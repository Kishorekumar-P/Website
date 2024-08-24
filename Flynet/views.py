from django.shortcuts import render
from django.core.mail import send_mail

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
    if request.method == "POST":
        f_name = request.POST.get("Fisrt name")
        l_name = request.POST.get("Last name")
        mobile_no = request.POST.get("Mobile Number")
        email = request.POST.get("E-mail")
        job_title = request.POST.get("Job Title")
        subject = request.POST.get("Subject")
        message = request.POST.get("Message")

        data = {
            'f_name': f_name,
            'l_name': l_name,
            'mobile_no': mobile_no,
            'email': email,
            'job_title': job_title,
            'subject': subject,
            'message': message
        }
        message ='''
        New message: {}

        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message,'',['kishorekumar10436@gmail.com'])
    return render(request, "contact.html")

def sub_services(request):
    return render(request, "sub_services.html")

def service_page(request):
    return render(request, "service_page.html")

def sub_services2(request):
    return render(request, "sub_services2.html")

def sub_services3(request):
    return render(request, "sub_services3.html")

def sub_services4(request):
    return render(request, "sub_services4.html")

def sub_services5(request):
    return render(request, "sub_services5.html")

def sub_services6(request):
    return render(request, "sub_services6.html")

def sub_services7(request):
    return render(request, "sub_services7.html")
 
def Blog_page(request):
    return render(request, "Blog_page.html")
