from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Extra", {"fields": ("phone_number", "birthday", "sex", "favorite_books", "is_admin")}),
    )
    filter_horizontal = ("favorite_books",)
