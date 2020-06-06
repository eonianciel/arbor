from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

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

    def get(self, request):
        form = self.form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form(request.POST, files=request.FILES)

        user=request.user

        if bound_form.is_valid():
            new_obj = bound_form.save(commit=False)
            new_obj.user=user
            new_obj.save()  
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(instance=obj)
        return render(request, self.template, context={'form': bound_form,
        self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            new_obj.author = request.user
            obj.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form,
        self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template,
         context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
