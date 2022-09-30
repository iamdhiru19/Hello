
from django.shortcuts import render, HttpResponse

from home.models import Contact


# Create your views here.
def index(request):
    context = {
        "variable": "this is sent"
    }
    return render(request, "index.html", context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, "about.html")
    # return HttpResponse("this is about page")

def services(request):
    # return HttpResponse("this is services page")
    return render(request, "services.html")

def contact(request):
    # return HttpResponse("this is contact page")
    if request.method == "POST" :
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        contact = Contact(name = name, phone = phone, email= email)
        contact.save()
    return render(request, "contact.html")
