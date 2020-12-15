from django.urls import reverse_lazy
from django.views.generic import CreateView

from books.models import Author
from django.contrib.auth.mixins import LoginRequiredMixin


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    template_name = "books/form_author_genre.html"
    success_url = reverse_lazy('bookstore')
    fields = '__all__'

