from django.shortcuts import render
from .models import Book

def home(request):
    books = Book.objects.all().order_by("-created_at")
    return render(request, "base.html", {"book":books})
