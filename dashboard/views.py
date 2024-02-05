from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def index(request):
    context = {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
    }
    return render(request,"dashboard/dashboard.html",context)

# def index(request):
#     if request.user.is_authenticated:
#         return redirect("dashboard-home")
#     else:
#         return redirect("login")