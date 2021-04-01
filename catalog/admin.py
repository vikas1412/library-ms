from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language


admin.site.register((Book, Author, Genre, BookInstance, Language))