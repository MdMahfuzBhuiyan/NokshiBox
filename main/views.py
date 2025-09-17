#This is a module & we are having a lot of functions
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def base(request):
    return render(request,'base.html')