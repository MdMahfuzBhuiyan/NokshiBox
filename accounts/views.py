# accounts/views.py
from django.contrib import messages
from django.shortcuts import render
from accounts.forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, 'Account created successfully!')
            form = UserForm()  # Clear form after success

    else:
        form = UserForm()

    return render(request, 'accounts/register.html', {'form': form})


def home(request):
    return render(request, 'main/home.html')  # use the correct path here

