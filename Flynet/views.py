from django.shortcuts import render

def home(request):
    return render(request, "Homepage.html")

def About_us(request):
    return render(request, "About_us.html")

def Homepage(request):
    return render(request, "Homepage.html")

def service(request):
    return render(request, "service.html")

def Blog_and_gallery(request):
    return render(request, "Blog_and_gallery.html")

def contact(request):
    return render(request, "contact.html")

def sub_services(request):
    return render(request, "sub_services.html")

def service_page(request):
    return render(request, "service_page.html")

