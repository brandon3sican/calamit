from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_user(request):
    if request.user.is_authenticated:
        return redirect("dashboard-home")    
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('dashboard-home')
        else:
            messages.info(request,"There was an error logging in, Try Again")
            return redirect('login')
        
    else:
        return render(request,'authenticate/login.html')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_user(request):
    logout(request)
    return redirect ('login')
