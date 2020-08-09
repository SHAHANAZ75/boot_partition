from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request,"base.html")
def signup(request):
    return render(request,"myapp/signup.html")
def login(request):
    return render(request,"myapp/login.html")

