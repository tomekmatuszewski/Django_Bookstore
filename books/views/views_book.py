from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from books.forms import BookForm
from books.models import Author, Book, Genre

from .books_filters import BookFilter, filter_books
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/books.html"
    context_object_name = "books"
    ordering = ["title"]
    paginate_by = 6

    def get_queryset(self):
        genre = self.request.GET.get("genre")
        author = self.request.GET.get("author")
        title = self.request.GET.get("title")
        min_rating = self.request.GET.get("rating-min")
        max_rating = self.request.GET.get("rating-max")
        if any([genre, author, title, min_rating, max_rating]):
            context = filter_books(
                genre=genre,
                author=author,
                title=title,
                max_rating=max_rating,
                min_rating=min_rating,
            )
            return context
        else:
            return super().get_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        context["authors"] = Author.objects.all()
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


# list view created for Django Filters
class BookListViewDF(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/books_df.html"
    ordering = ["title"]
    paginate_by = 6

    def paginate_filter_queryset(self):
        context = BookFilter(self.request.GET, queryset=self.get_queryset()).qs
        paginate_by = self.get_paginate_by(context)
        page = self.request.GET.get('page', 1)

        paginator = Paginator(context, paginate_by)

        try:
            paginated_filter = paginator.page(page)
        except PageNotAnInteger:
            paginated_filter = paginator.page(1)
        except EmptyPage:
            paginated_filter = paginator.page(paginator.num_pages)
        return paginated_filter

    def get_paginate_by(self, queryset):
        if self.request.GET.get("paginate_by") == "":
            return self.paginate_by
        return self.request.GET.get("paginate_by", self.paginate_by)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = BookFilter(self.request.GET, queryset=self.get_queryset())
        context["paginated_filter"] = self.paginate_filter_queryset()
        return context


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("bookstore")
    permission_required = "books.add_book"


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    permission_required = "books.change_book"

    def get_success_url(self):
        return reverse_lazy("book-detail", kwargs={"pk": self.request.object.pk})

    def get_permission_denied_message(self):
        return messages.error(
            self.request, "You have no permission to update this book!"
        )

    def handle_no_permission(self):
        self.get_permission_denied_message()
        return HttpResponseRedirect(reverse_lazy("bookstore"))


class BookDeleteView(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("books")
