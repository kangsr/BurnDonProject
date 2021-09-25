from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def login(req):
    if req.method == "POST":
        form = AuthenticationForm(request=req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=req, username=username, password=password)
            if user is not None:
                auth.login(req, user)
                return redirect("home")
            else:
                return HttpResponse('Login failed. Try again.')
    else:
        form = AuthenticationForm()

    return render(req, "login.html", {"form": form})


def logout_view(req):
    logout(req)
    return redirect("home")

def resister_veiw(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
        return redirect("home")
    else:
        form = UserCreationForm()
        return render(req, "signup.html", {"form": form})