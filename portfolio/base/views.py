from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home(request): 
    img = Brands.objects.all()
    portfolio = Work.objects.all()
    context = {
        "portfolio": portfolio,
        "imgs": img,
    }    
    return render(request, 'home.html', context) 


def service(request):
    serv = Service.objects.all()
    context = {
        "serv": serv,
    }

    return render(request, 'service.html', context)


def testimonials(request):
    more_testimony = Other_Testimonials.objects.all()
    testimony = Testimonials.objects.all()
    context = {
        "mt": more_testimony,
        "test": testimony,
    }
    return render(request, 'testimonials.html', context)




def contact(request):
    context = {}

    return render(request, 'contact.html', context)