from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from books.models import Book
from books.forms import BookForm


class BookListView(ListView):

    model = Book
    template_name = "books/books.html"
    context_object_name = "books"
    ordering = ["title"]
    paginate_by = 6


class BookCreateView(CreateView):

    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy('bookstore')

