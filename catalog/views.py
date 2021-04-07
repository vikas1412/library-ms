import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from catalog.forms import RenewBookForm
from catalog.models import BookInstance, Book, Genre, Language, Author
from django.views import generic


@login_required
@permission_required('can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':
        form = RenewBookForm(request.POST)

        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            return HttpResponseRedirect(reverse('index'))

    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }
    return render(request, 'catalog/book_renew_librarian.html', context)


def index(request):

    total_book_instance = BookInstance.objects.all()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    available_books = BookInstance.objects.filter(status__exact='a').count()
    authors = Author.objects.all()
    total_books = Book.objects.all()
    params = {
        'available_books': available_books,
        'authors': authors,
        'books': total_books,
        'total_copies': total_book_instance,
        'num_visits': num_visits,
    }
    return render(request, 'catalog/index.html', params)


class BookListView(generic.ListView):
    model = Book
    template_name = "catalog/all_books.html"
    context_object_name = "book_instance"
    paginate_by = 4

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


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/all_authors.html'
    context_object_name = 'authors'
    paginate_by = 4


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'
    context_object_name = 'author'