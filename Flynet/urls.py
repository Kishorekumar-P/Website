from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("Homepage",views.Homepage, name="Homepage"),
    path("About_us",views.About_us, name="About_us"),
    path("service",views.service, name="service"),
    path("Blog_and_gallery",views.Blog_and_gallery, name="Blog_and_gallery"),
    path("contact",views.contact, name="contact"),



]
                                                                                                                                                                      