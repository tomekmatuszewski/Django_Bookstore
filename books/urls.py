from django.urls import path
from books.views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('bookstore/', BookListView.as_view(), name="bookstore"),
    path('bookstore/add-book/', BookCreateView.as_view(), name="book-add"),
    path('bookstore/book/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('bookstore/book/<int:pk>/update/', BookUpdateView.as_view(), name="book-update"),
    path('bookstore/book/<int:pk>/delete/', BookDeleteView.as_view(), name="book-delete"),

]