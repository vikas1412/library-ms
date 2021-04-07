from django.urls import path
from catalog import views
from catalog.views import BookListView


urlpatterns = [
    path('', views.index, name="index"),
    path('books/', BookListView.as_view(), name="books"),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name="book-detail"),

    path('authors/', views.AuthorListView.as_view(), name="authors"),
    path('author/<str:name>/<int:pk>', views.AuthorDetailView.as_view(), name="author-detail"),

    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

    path('borrower/', views.LoanedBooksByUserListView.as_view(), name='all-borrowers')
]