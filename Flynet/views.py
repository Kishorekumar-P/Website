from django.shortcuts import render

def home(request):
    return render(request, "Homepage.html")

def About_us(request):
    return render(request, "About_us.html")

def Homepage(request):
    return render(request, "Homepage.html")

def service(request):
    return render(request, "service.html")
