from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index") 
        else:
            error = "نام کاربری یا رمز عبور اشتباه است"
            return render(request, "sign_in.html", {"error": error})
    return render(request, "sign_in.html")

def index(request):
    return render(request, 'accounts/base.html')
