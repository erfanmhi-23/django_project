from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm

def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/books/home/')
        else:
            error = "نام کاربری یا رمز عبور اشتباه است"
            return render(request, "accounts/sign_in.html", {"error": error})
    return render(request, "accounts/sign_in.html")

def index(request):
    return render(request, 'accounts/base.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def sign_in(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('books:home')
        else:
            error = "کاربر یا رمز عبور اشتباه است"
            return render(request, "accounts/sign_in.html", {"error": error})
    return render(request, "accounts/sign_in.html")

def logout_view(request):
    logout(request)
    return redirect('index')

def profile_view(request):
    user = request.user
    if request.method == "POST":
        form = UserRegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserRegisterForm(instance=user)

    return render(request, "accounts/profile.html", {"form": form})
