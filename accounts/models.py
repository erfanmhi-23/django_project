from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True, unique=True)
    birthday = models.DateField(blank=True, null=True)
    SEX_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    favorite_books = models.ManyToManyField('books.Book', blank=True, related_name="favorited_by")

    def save(self, *args, **kwargs):
        self.is_staff = True  
        self.is_superuser = True  
        self.is_admin = True
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.get_full_name()or self.username
    
