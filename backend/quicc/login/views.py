from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse


def login(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        remember_me = req.POST.get("remember_me")
        print(remember_me)
        user = authenticate(req, username=username, password=password)
        if user is not None:

            auth_login(req, user)

            if user.role == "E":
                response = redirect("/employee/")
            elif user.role == "M":
                response = redirect("/manager/")

            if remember_me == "on":
                # Set cookie expiration to a longer duration (e.g., 30 days)
                print("remember me is on")
                req.session.set_expiry(3600 * 24 * 15)
                response.set_cookie("remember_me", "true", max_age=3600 * 24 * 15)
                return response
            else:
                # Set session expiration to default (usually browser session)
                req.session.set_expiry(0)
                return response
        else:
            return HttpResponse("Invalid login")
    else:
        print("hola")
        if req.user.is_authenticated:
            print("I AM AUTHER")
            if req.user.role == "E":
                response = redirect("/employee/")
            elif req.user.role == "M":
                response = redirect("/manager/")
            return response
        else:
            print("not auth")
            return render(req, "login/login_page.html")


def logout_view(req):
    logout(req)
    # Redirect to a page after logout, for example, the homepage
    res = redirect("/")
    if "remember_me" in req.COOKIES:
        res.delete_cookie("remember_me")
    return res
