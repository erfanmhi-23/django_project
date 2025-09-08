from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="book_rating")
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="ratings")
    rate = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinLengthValidator(0.0), MaxLengthValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "book")

    def __str__(self):
        return (f"{self.user} -> {self.book}: {self.rate}")





