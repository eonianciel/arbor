from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Famille
from .forms import PostForm, FamilleForm
from .utils import*


@login_required
def famille_list(request):
    familles = Famille.objects.all()
    return render(request, 'tree/famille_list.html', context={'familles': familles})

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'tree/post_list.html', {'posts': posts})


class PostDetail(LoginRequiredMixin, ObjectDetailMixin, View):
    model = Post
    template = 'tree/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
        model = Post
        form = PostForm
        template = 'tree/post_create.html'


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
        model = Post
        form = PostForm
        template = 'tree/post_edit.html'


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin,View):
    model = Post
    template = 'tree/post_delete.html'
    redirect_url = 'post_list'


class FamilleDetail(LoginRequiredMixin, ObjectDetailMixin, View):
    model = Famille
    template = 'tree/famille_detail.html'


class FamilleCreate(LoginRequiredMixin, ObjectCreateMixin, View):
        model = Famille
        form = FamilleForm
        template = 'tree/famille_create.html'


class FamilleUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
        model = Famille
        form = FamilleForm
        template = 'tree/famille_edit.html'


class FamilleDelete(LoginRequiredMixin, ObjectDeleteMixin,View):
    model = Famille
    template = 'tree/famille_delete.html'
    redirect_url = 'famille_list'
