from django.urls import path

from .views import*

urlpatterns = [
    path('image/', image_list, name='image_list'),
    path('images/create/', image_create, name='image_create'),
    path('images/detail/<int:id>/<slug:slug>/', image_detail, name='image_detail'),
]
