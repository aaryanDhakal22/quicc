from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse


def login(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        remember_me = req.POST.get("remember_me")
        user = authenticate(req, username=username, password=password)
        if user is not None:

            auth_login(req, user)

            if user.role == "E":
                response = redirect("/employee/")
            elif user.role == "M":
                response = redirect("/manager/")

            if remember_me == "on":
                # Set to expire after 15 days
                req.session.set_expiry(3600 * 24 * 15)
                return response
            else:
                # Set to expire after browser close
                req.session.set_expiry(0)
                return response
        else:
            return HttpResponse("Invalid login")
    else:
        if req.user.is_authenticated:
            if req.user.role == "E":
                response = redirect("/employee/")

            elif req.user.role == "M":
                response = redirect("/manager/")
            return response
        else:
            return HttpResponse("Login Successfull")


def logout_view(req):
    logout(req)
    res = redirect("/")
    return res
