from django.shortcuts import render, redirect, get_object_or_404

from .models import*


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template,
        context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    model = None
    form = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post_new(self, request):
        if request.method == "POST":
            bound_form = self.form(request.POST)
            if bound_form.is_valid():
                obj = bound_form.save(commit=False)
                obj.author = request.user
                obj.save()
                return redirect(self.redirect_url, 'slug'==obj.slug)
        else:
            bound_form = self.form()
        return render(request, self.template, {'form': bound_form})

"""
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', 'slug'==post.slug)
    else:
        form = PostForm()
    return render(request, 'tree/post_edit.html', {'form': form})
"""

class ObjectUpdateMixin:
    model = None
    form = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post_edit(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        if request.method == "POST":
            bound_form = self.form(request.POST, instance=obj)
            if bound_form.is_valid():
                obj = bound_form.save(commit=False)
                obj.author = request.user
                obj.save()
                return redirect(self.redirect_url, 'slug'==obj.slug)
        else:
            bound_form = self.form(instance=obj)
        return render(request, self.template, {'form': bound_form})

"""
def post_edit(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', 'slug'==post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'tree/post_edit.html', {'form': form})
"""


class ObjectPublicateMixin:
    model = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, context={self.model.__name__.lower(): obj})

    def post_publish(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj.publish()
        return redirect(self.redirect_url, slug__iexact=slug)

"""
def post_publish(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    post.publish()
    return redirect('post_detail', slug__iexact=slug)
    """


class ObjectDeleteMixin:
    model = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, context={self.model.__name__.lower(): obj})

    def post_remove(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj.delete()
        return redirect(self.redirect_url)

"""
def post_remove(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    post.delete()
    return redirect('post_list')
    """
