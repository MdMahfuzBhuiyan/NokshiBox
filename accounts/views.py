from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from accounts.forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


User = get_user_model()

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or any other valid route name
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, email=email, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            messages.success(request, "You are now logged in")

            return redirect('/accounts/dashboard/')  
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login') 
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged out')
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
