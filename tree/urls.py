from django.contrib import admin
from django.urls import path

from .views import*

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', PostCreate.as_view(), name='post_new'),
    path('post/<str:slug>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('post/<str:slug>/publish/', PostPublish.as_view(), name='post_publish'),
    path('post/<str:slug>/remove/', PostDelete.as_view(), name='post_remove'),
    path('famille/', famille_list, name='famille_list'),
    path('famille/<str:slug>/', FamilleDetail.as_view(), name='famille_detail'),
]
