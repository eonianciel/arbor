from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.utils import timezone
from django.urls import reverse

from .models import Post, Famille
from .forms import PostForm, FamilleForm
from .utils import*

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'tree/post_list.html', {'posts': posts})

def famille_list(request):
    familles = Famille.objects.all()
    return render(request, 'tree/famille_list.html', context={'familles': familles})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'tree/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
        model = Post
        form = PostForm
        template = 'tree/post_create.html'


class PostUpdate(ObjectUpdateMixin, View):
        model = Post
        form = PostForm
        template = 'tree/post_edit.html'
        redirect_url = 'post_detail'


class PostDelete(ObjectDeleteMixin,View):
    model = Post
    template = 'tree/post_delete.html'
    redirect_url = 'post_list'


class FamilleDetail(ObjectDetailMixin, View):
    model = Famille
    template = 'tree/famille_detail.html'


class FamilleCreate(ObjectCreateMixin, View):
        model = Famille
        form = FamilleForm
        template = 'tree/famille_edit.html'


class FamilleUpdate(ObjectUpdateMixin, View):
        model = Famille
        form = FamilleForm
        template = 'tree/famille_edit.html'
        redirect_url = 'famille_detail'


class FamilleDelete(ObjectDeleteMixin,View):
    model = Famille
    template = 'tree/famille_delete.html'
    redirect_url = 'famille_list'
