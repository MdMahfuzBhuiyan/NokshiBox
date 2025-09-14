#This is a module & we are having a lot of functions
from django.shortcuts import render
from django.http import HttpResponse


def home (request):
    return render(request,'home.html')