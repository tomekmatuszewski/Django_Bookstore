from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from books.models import Genre
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class StaffRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


class GenreCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Genre
    template_name = "books/form_author_genre.html"
    fields = '__all__'
    permission_required = 'books.add_genre'

    def get_success_url(self):
        messages.success(self.request, "New genre successfully added")
        return reverse_lazy('genres')


class GenreListView(ListView):
    model = Genre
    template_name = 'books/genre_list.html'
    context_object_name = 'genres'


class GenreUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Genre
    template_name = "books/form_author_genre.html"
    fields = '__all__'
    success_url = reverse_lazy('genres')
    permission_required = 'books.change_genre'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Genre data successfully changed")
        return super().form_valid(form)


class GenreDeleteView(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Genre
    template_name = "books/genre_confirm_delete.html"

    def get_success_url(self):
        messages.error(self.request, "Genre successfully deleted")
        return reverse_lazy('genres')