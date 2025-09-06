from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required


def home(request):
    books = Book.objects.all()
    return render(request, "home.html")