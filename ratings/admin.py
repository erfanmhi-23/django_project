from django.contrib import admin
from .models import Rating

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "rate", "created_at")
    search_fields = ("user__username", "book__title")
    list_filter = ("rate",)

