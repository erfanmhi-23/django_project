from django.urls import path
from .views import register_view, sign_in, index, profile_view, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('register/', register_view, name='register'),
    path('login/', sign_in, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),

]
