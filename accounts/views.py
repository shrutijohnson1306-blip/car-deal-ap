from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect("login")   # redirects to Django's built-in login
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

def custom_logout(request):
    """Logout user via GET and redirect home"""
    logout(request)
    return redirect("/")

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, "home.html")