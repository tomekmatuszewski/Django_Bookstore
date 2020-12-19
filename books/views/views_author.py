from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from books.models import Author


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class AuthorCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Author
    template_name = "books/form_author_genre.html"
    fields = "__all__"
    permission_required = "books.add_author"


    def get_success_url(self):
        messages.success(self.request, "New author successfully added")
        return reverse_lazy("authors")


class AuthorListView(ListView):
    model = Author
    template_name = "books/authors_list.html"
    context_object_name = "authors"


class AuthorUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Author
    template_name = "books/form_author_genre.html"
    fields = "__all__"
    success_url = reverse_lazy("authors")
    permission_required = "books.change_author"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Author data successfully changed")
        return super().form_valid(form)


class AuthorDeleteView(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Author
    template_name = "books/author_confirm_delete.html"

    def get_success_url(self):
        messages.error(self.request, "Author data successfully deleted")
        return reverse_lazy("authors")
