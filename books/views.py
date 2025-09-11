from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Favorite
from django.core.paginator import Paginator
from django.db.models import Q
from authors.models import Author
from categories.models import Category
from django.contrib import messages
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt


def home(request):
    latest_books = Book.objects.order_by('-id')[:5] 
    return render(request, 'home.html', {'latest_books': latest_books})


def book_list(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    categories = Category.objects.all()

    author_id = request.GET.get("author")
    if author_id:
        books = books.filter(author__id=author_id)

    category_id = request.GET.get("category")
    if category_id:
        books = books.filter(category__id=category_id)

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

    group_by_category = request.GET.get('group_by_category') == 'on'
    if group_by_category:
        category_books = {category: category.books.filter(
            id__in=books.values_list('id', flat=True)
        ) for category in categories}
        context = {
            'group_by_category': True,
            'category_books': category_books,
            'authors': authors,
            'categories': categories,
        }
    else:
        paginator = Paginator(books, 14)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            'group_by_category': False,
            'page_obj': page_obj,
            'authors': authors,
            'categories': categories,
        }

    return render(request, "book_list.html", context)



def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, book=book).exists()

    return render(request, 'book_detail.html', {'book': book,'is_favorite': is_favorite})

def search_books(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query) |
            Q(code__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
    return render(request, 'search_resultes.html', {'results': results, 'query': query})


def about(request):
    return render(request, 'about.html')


def call(request):
    return render(request, 'call.html')

def toggle_favorite(request, book_id):
    if not request.user.is_authenticated:
        messages.error(request, " ابتدا باید وارد حساب کاربری خود شوید.")
        return redirect("home")

    book = get_object_or_404(Book, id=book_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, book=book)

    if not created:
        favorite.delete()
        messages.success(request, f"«{book.title}» از علاقه‌مندی‌ها حذف شد.")
    else:
        messages.success(request, f"«{book.title}» به علاقه‌مندی‌ها اضافه شد.")

    return redirect(request.META.get("HTTP_REFERER", "home"))


def favorites_list(request):
    if not request.user.is_authenticated:
        messages.error(request, "⚠️ ابتدا باید وارد حساب کاربری خود شوید.")
        return redirect("home")

    favorite_books = Book.objects.filter(book_favorites__user=request.user).distinct()
    return render(request, "favorites_list.html", {"favorite_books": favorite_books})

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('home')
   
def accounts_redirect(request):
    return redirect('home')