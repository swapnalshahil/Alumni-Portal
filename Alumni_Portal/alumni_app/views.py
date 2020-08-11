from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



# Create your views here.
# test test12345

def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    #return HttpResponse("hello")
    print(request.user)
    return render(request,'alumni_app/home.html')

def loginUser(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(password)
        user=authenticate(username=username,password=password)    
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")     
        else:
            return render(request,'alumni_app/login.html')
    
    
    return render(request,'alumni_app/login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")
    #return render(request,'alumni_app/logout.html')






