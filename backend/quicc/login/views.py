from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse


# Create your views here.
def login_page(req):
    return render(req, "staff/login.html")


def login(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        print(username, password)
        user = authenticate(req, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(req, user)
            if user.is_employee:
                return redirect("/employee/")
            elif user.is_manager:
                return redirect("/manager/")
        else:
            return HttpResponse("Invalid login")
    else:
        return render(req, "login.html")
