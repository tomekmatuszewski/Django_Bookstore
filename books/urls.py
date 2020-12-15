from django.urls import path
from books.views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView, AuthorCreateView,GenreCreateView

urlpatterns = [
    path('bookstore/', BookListView.as_view(), name="bookstore"),
    path('bookstore/add-book/', BookCreateView.as_view(), name="book-add"),
    path('bookstore/book/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('bookstore/book/<int:pk>/update/', BookUpdateView.as_view(), name="book-update"),
    path('bookstore/book/<int:pk>/delete/', BookDeleteView.as_view(), name="book-delete"),
    path('bookstore/author/create/', AuthorCreateView.as_view(), name="author-add"),
    path('bookstore/genre/create/', GenreCreateView.as_view(), name="genre-add"),

]