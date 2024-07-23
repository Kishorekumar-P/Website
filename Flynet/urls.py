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
    path("sub_services",views.sub_services, name="sub_services"),
    path("service_page",views.service_page, name="service_page"),
    path("sub_services2",views.sub_services2, name="sub_services2"),
    path("sub_services3",views.sub_services3, name="sub_services3"),
    path("sub_services4",views.sub_services4, name="sub_services4"),
    path("sub_services5",views.sub_services5, name="sub_services5"),
    path("sub_services6",views.sub_services6, name="sub_services6"),
    path("sub_services7",views.sub_services7, name="sub_services7"),
    path("Blog_page",views.Blog_page, name="Blog_page"),




]
                                                                                                                                                                      