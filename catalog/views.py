from django.shortcuts import render
from catalog.models import BookInstance, Book, Genre, Language, Author
from django.views import generic


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


class BookListView(generic.ListView):
    model = Book
    template_name = "catalog/all_books.html"
    context_object_name = "book_instance"

    def get_queryset(self):
        """Override to implement additional functionality like 'objects.filter()' instead of 'objects.all()'"""
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        """Override this method to pass more than 1 arguments
        * First get the existing context from our superclass.
        * Then add your new context information.
        * Then return the new (updated) context.
        """
        context = super(BookListView, self).get_context_data(**kwargs)
        context['total_books_demo'] = Book.objects.all().count()
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
    context_object_name = 'book'


def all_authors(request):
    all_authors = Author.objects.all()
    params = {
        'authors': all_authors,
    }
    return render(request, 'catalog/all_authors.html', params)