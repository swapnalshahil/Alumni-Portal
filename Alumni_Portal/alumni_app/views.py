from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
# test test12345

def home(request):
    
    #return HttpResponse("hello")
    return render(request,'alumni_app/index.html')

def login(request):
    return render(request,'alumni_app/login.html')

def logout(request):
    return render(request,'alumni_app/logout.html')






