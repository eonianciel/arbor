from django.urls import path

from .views import*

urlpatterns = [
    path('images/create/', image_create, name='image_create'),
    path('images/detail/<int:id>/<slug:slug>/', image_detail, name='image_detail'),
]
