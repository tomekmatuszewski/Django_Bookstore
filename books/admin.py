from django.contrib import admin
from books.models import Author, Genre, Book

# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
