from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.utils import timezone
from django.urls import reverse

from .models import Post
from .forms import PostForm
from .utils import*

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'tree/post_list.html', {'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'tree/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
        model = Post
        form = PostForm
        template = 'tree/post_edit.html'
        redirect_url = 'post_detail'


class PostUpdate(ObjectUpdateMixin, View):
        model = Post
        form = PostForm
        template = 'tree/post_edit.html'
        redirect_url = 'post_detail'


class PostPublish(ObjectPublicateMixin, View):
    model = Post
    redirect_url = 'post_detail'


class PostDelete(ObjectDeleteMixin,View):
    model = Post
    redirect_url = 'post_list'
