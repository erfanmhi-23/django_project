from django.db import models
from django.db.models import Avg

class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.ManyToManyField("authors.Author", related_name="books", blank=True)
    code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    category = models.ForeignKey("categories.category", on_delete=models.SET_NULL, null=True, blank=True, related_name="books")
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="covers/", blank=True, null=True)
    language = models.CharField(max_length=50 , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def average_rating(self):
        agg = self.ratings.aggregate(avg=Avg("rate"))
        return agg["avg"] or 0.0
    
    def __str__(self):
        return self.title
