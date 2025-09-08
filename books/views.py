from django.shortcuts import render , get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from authors.models import Author


def home(request):
    latest_books = Book.objects.order_by('-id')[:3] 
    return render(request, 'home.html', {'latest_books': latest_books})

def book_list(request):
    books = Book.objects.all().order_by("-id")
    authors = Author.objects.all()

    author_id = request.GET.get("author")
    if author_id:
        books = books.filter(author__id=author_id)

    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    if min_price:
        books = books.filter(price__gte=min_price)
    if max_price:
        books = books.filter(price__lte=max_price)

    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    if start_date:
        books = books.filter(published_date__gte=start_date)
    if end_date:
        books = books.filter(published_date__lte=end_date)

    paginator = Paginator(books, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "book_list.html", {"page_obj": page_obj, "authors": authors})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})


def search_books(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Book.objects.filter(Q(title__icontains=query) |Q(author__first_name__icontains=query) |Q(author__last_name__icontains=query)).distinct()
    return render(request, 'search_resultes.html', {'results': results, 'query': query})