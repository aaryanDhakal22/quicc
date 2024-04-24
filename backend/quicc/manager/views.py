from django.shortcuts import render


# Create your views here.
def manager_home_page(req):
    username = req.user.username
    role = req.user.role
    if role == "E":
        role = "Employee"
    else:
        role = "Manager"
    context = {"username": username, "role": role}
    return render(req, "manager/homepage.html", context)
