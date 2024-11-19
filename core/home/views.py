from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from mainapp.models import *


def home(request):

   services = Service.objects.all()

   for service in services:
      print(service.Sname)

   return render(request,"index.html",context= {"services" : services})
