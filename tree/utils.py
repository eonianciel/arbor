from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import*


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    model = None
    form = None
    template = None

    def get(self, request):
        form = self.form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})

"""
        if bound_form.is_valid():
            new_obj = bound_form.save(commit=False)
            new_obj.author = request.user
            new_obj.save()
            return redirect('post_detail', 'slug'==new_obj.slug)
        else:
            form = self.form()
        return render(request, self.template, {'form': bound_form})


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
    redirect_url =None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save(commit=False)
            #new_obj.author = request.user
            #obj.save()
            return redirect(self.redirect_url, 'slug'==new_obj.slug)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


"""
class ObjectUpdateMixin:
    model = None
    form = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model()
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
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


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))

"""
def post_remove(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    post.delete()
    return redirect('post_list')
    """
