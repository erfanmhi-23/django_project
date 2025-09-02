from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    birthday = models.DateField(blank=True, null=True)
    is_dead = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    categories = models.ManyToManyField("categories.Category", blank=True, related_name="authors")

    def __str__(self):
        return (f"{self.first_name} {self.last_name}").strip()









