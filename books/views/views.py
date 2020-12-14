from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"

    def get_success_url(self):
        return reverse_lazy('book-detail', kwargs={'pk': self.request.object.pk})


class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy('books')
