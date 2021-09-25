from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

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