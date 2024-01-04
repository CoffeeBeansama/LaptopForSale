from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . import models

# Create your views here.

def home(request):
    return HttpResponse(loader.get_template("home.html").render({},request))
