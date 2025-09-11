from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.book_list, name="book_list"),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('search/', views.search_books, name='search_books'),
    path("about/" ,views.about , name= "about" ),
    path("call/" ,views.call , name= "call" ),
    path("toggle-favorite/<int:book_id>/", views.toggle_favorite, name="toggle_favorite"),
    path("favorites/", views.favorites_list, name="favorites_list"),
    path("logout/", views.logout_view, name="logout"),
    path("accounts/", views.accounts_redirect, name="accounts_redirect"),
]

