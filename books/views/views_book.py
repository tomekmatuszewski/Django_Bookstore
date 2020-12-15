from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from books.models import Book, Genre, Author
from books.forms import BookForm



class BookListView(ListView):
    model = Book
    template_name = "books/books.html"
    context_object_name = "books"
    ordering = ["title"]
    paginate_by = 6

    def get_queryset(self):
        genre = self.request.GET.get('genre')
        author = self.request.GET.get('author')
        if genre:
            new_context = self.model.objects.filter(genre=Genre.objects.get(name=genre))
            return new_context
        elif author:
            first_name = author.split(' ')[0]
            last_name = author.split(' ')[1]
            new_context = self.model.objects.filter(author=Author.objects.get(first_name=first_name,
                                                                              last_name=last_name))
            return new_context
        else:
            return super().get_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['authors'] = Author.objects.all()
        return context

    def get_paginate_by(self, queryset):
        super().get_paginate_by(queryset)
        return self.request.GET.get('paginate_by', self.paginate_by)


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
