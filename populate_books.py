import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from books.models import Book
from authors.models import Author
from categories.models import Category

fake = Faker()

# گرفتن همه نویسنده‌ها و دسته‌بندی‌ها
authors = list(Author.objects.all())
categories = list(Category.objects.all())

for _ in range(100):
    book = Book.objects.create(
        title=fake.sentence(nb_words=4),
        price=round(random.uniform(10, 200), 2),
        published_date=fake.date_between(start_date='-10y', end_date='today'),
        pages=random.randint(50, 1000),
        description=fake.paragraph(nb_sentences=3),
        language=random.choice(['فارسی', 'انگلیسی', 'فرانسه', 'آلمانی']),
        image=None  # یا می‌تونی عکس پیش‌فرض بذاری
    )

    # اضافه کردن نویسنده‌ها (با بررسی تعداد واقعی)
    if authors:
        num_authors = min(len(authors), random.randint(1, 3))
        book.author.add(*random.sample(authors, k=num_authors))

    # اضافه کردن دسته‌بندی‌ها
    if categories:
        book.category = random.choice(categories)
        book.save()

print("✅ 100 کتاب فیک ساخته شد!")
