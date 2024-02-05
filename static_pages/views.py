from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def project1(request):
    return render(request,"project-1.html")

def project2(request):
    return render(request,"project-2.html")