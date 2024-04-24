from django.shortcuts import render, redirect
from login.models import User


# Create your views here.
def employee_home_page(req):
    username = req.user.username
    role = req.user.role
    clocked_in = req.user.is_clocked_in
    if role == "E":
        role = "Employee"
    else:
        role = "Manager"
    if clocked_in:
        clocked_in = "Clock Out"
    else:
        clocked_in = "Clock In"
    context = {"username": username, "role": role, "clocked_in": clocked_in}
    return render(req, "employee/homepage.html", context)


def toggle_clock(req, username):
    user = User.objects.get(username=username)
    if user.is_clocked_in:
        user.is_clocked_in = False
    else:
        user.is_clocked_in = True
    user.save()
    print(user.is_clocked_in)
    return redirect("employee_home")
