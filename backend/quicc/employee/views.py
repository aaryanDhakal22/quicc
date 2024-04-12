from django.shortcuts import render


# Create your views here.
def employee_home_page(req):
    username = req.user.username
    role = req.user.role
    if role == "E":
        role = "Employee"
    else:
        role = "Manager"
    context = {"username": username, "role": role}
    return render(req, "employee/homepage.html", context)
