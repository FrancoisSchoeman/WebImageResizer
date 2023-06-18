from django.urls import path
from . import views

urlpatterns = [
    path("", views.resize_image, name="resize_image"),
    path("contact/", views.contact, name="contact"),
]
