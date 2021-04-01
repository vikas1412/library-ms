from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('all-books/', views.all_books, name="all_books"),
    path('all-authors/', views.all_authors, name="all-authors"),
]