from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =("title", "get_author" , "category", "price", "published_date")
    search_fields = ("title", "authors__first_name", "authors__last_name", "language" , "code")
    list_filter = ("category" , "published_date" )
    filter_horizontal =("author",)

    def get_author(self, obj):
        return ", ".join([str(a) for a in obj.author.all()])
    get_author.short_description = "Author"





