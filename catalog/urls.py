from django.urls import path
from catalog import views
from catalog.views import BookListView

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', BookListView.as_view(), name="books"),

    path('authors/', views.all_authors, name="authors"),
]