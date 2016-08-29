from django.shortcuts import render,redirect
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy,reverse
from datetime import datetime

# Create your views here.
def index(request):
    year = datetime.today().year
    return render(request,'index.html',{"year":year})
def services(request):
    year = datetime.today().year
    return render(request,'services.html',{"year":year})
def about(request):
    year = datetime.today().year
    return render(request,'About.html',{"year":year})
def contact(request):
    year = datetime.today().year
    return render(request,'Contact.html',{"year":year})