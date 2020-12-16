from django.urls import reverse_lazy
from django.views.generic import CreateView

from books.models import Genre
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class GenreCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Genre
    template_name = "books/form_author_genre.html"
    success_url = reverse_lazy('bookstore')
    fields = '__all__'
    permission_required = 'books.add_genre'

