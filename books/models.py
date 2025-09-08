from django.db import models
from django.db.models import Avg
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.ManyToManyField("authors.Author", related_name="books", blank=True)
    code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books"
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="books/", blank=True, null=True)
    language = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def average_rating(self):
        agg = self.book_ratings.aggregate(avg=Avg("rate"))
        return agg["avg"] or 0.0

    def __str__(self):
        return self.title


class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_ratings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("user", "book")

    def __str__(self):
        return f"{self.user} -> {self.book}: {self.rate}"
