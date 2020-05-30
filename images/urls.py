from django.urls import path

from .views import*

urlpatterns = [
    path('images/create/', image_create, name='image_create'),
]
