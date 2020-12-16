from django.urls import path
from books.views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView, \
    AuthorCreateView,GenreCreateView, AuthorListView, AuthorUpdateView, AuthorDeleteView, GenreListView, \
    GenreUpdateView, GenreDeleteView

urlpatterns = [
    path('bookstore/books/', BookListView.as_view(), name="bookstore"),
    path('bookstore/book/add-book', BookCreateView.as_view(), name="book-add"),
    path('bookstore/book/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('bookstore/book/<int:pk>/update/', BookUpdateView.as_view(), name="book-update"),
    path('bookstore/book/<int:pk>/delete/', BookDeleteView.as_view(), name="book-delete"),

    path('bookstore/author/create/', AuthorCreateView.as_view(), name="author-add"),
    path('bookstore/authors/', AuthorListView.as_view(), name="authors"),
    path('bookstore/author/<int:pk>/update', AuthorUpdateView.as_view(), name="author-update"),
    path('bookstore/author/<int:pk>/delete', AuthorDeleteView.as_view(), name="author-delete"),

    path('bookstore/genre/create/', GenreCreateView.as_view(), name="genre-add"),
    path('bookstore/genres/', GenreListView.as_view(), name="genres"),
    path('bookstore/genre/<int:pk>/update/', GenreUpdateView.as_view(), name="genre-update"),
    path('bookstore/genre/<int:pk>/delete/', GenreDeleteView.as_view(), name="genre-delete"),

]