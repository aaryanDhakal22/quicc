from django.shortcuts import render


# Create your views here.
def login_page(req):
    return render(req, "staff/login.html")
