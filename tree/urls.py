from django.contrib import admin
from django.urls import path

from .views import*

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/new/', PostCreate.as_view(), name='post_new'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    #path('post/new/', PostCreate.as_view(), name='post_new'),
    path('post/<str:slug>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete'),
    path('famille/', famille_list, name='famille_list'),
    path('famille/<str:slug>/', FamilleDetail.as_view(), name='famille_detail'),
    path('famille/create', FamilleCreate.as_view(), name='famille_create'),
    path('famille/<str:slug>/update/', FamilleUpdate.as_view(), name='famille_update'),
    path('famille/<str:slug>/delete/', FamilleDelete.as_view(), name='famille_delete'),
]
