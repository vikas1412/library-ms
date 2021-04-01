from django.shortcuts import render
from catalog.models import BookInstance, Book, Genre, Language, Author

def index(request):

    total_book_instance = BookInstance.objects.all()
    available_books = BookInstance.objects.filter(status__exact='a').count()
    authors = Author.objects.all()
    total_books = Book.objects.all()
    params = {
        'available_books': available_books,
        'authors': authors,
        'books': total_books,
        'total_copies': total_book_instance,
    }
    return render(request, 'catalog/index.html', params)


def all_books(request):
    book_instance = Book.objects.all()
    params = {
        'book_instance': book_instance,
    }
    return render(request, 'catalog/all_books.html', params)


def all_authors(request):
    all_authors = Author.objects.all()
    params = {
        'authors': all_authors,
    }
    return render(request, 'catalog/all_authors.html', params)