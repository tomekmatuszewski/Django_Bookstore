from django.urls import path
from books.views import BookListView, BookCreateView

urlpatterns = [
    path('bookstore/', BookListView.as_view(), name="bookstore"),
    path('bookstore/add-book/', BookCreateView.as_view(), name="book-add"),

]