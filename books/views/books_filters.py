import django_filters
from django.forms import CheckboxInput
from django_filters.widgets import RangeWidget

from books.models import Author, Book, Genre

# based on django filters


class BookFilter(django_filters.FilterSet):

    CHOICES = (("ascending", "Ascending"), ("descending", "Descending"))

    title = django_filters.CharFilter(
        label="Title", field_name="title", lookup_expr="icontains"
    )

    genre = django_filters.ModelChoiceFilter(
        label="Genre", queryset=Genre.objects.all(), field_name="genre"
    )
    author = django_filters.ModelChoiceFilter(
        label="Author", queryset=Author.objects.all(), field_name="authors"
    )

    ordering = django_filters.ChoiceFilter(
        label="Ordering by Price", choices=CHOICES, method="filter_by_order"
    )

    rating = django_filters.RangeFilter(
        label="Rating Between",
        field_name="rating",
        widget=RangeWidget(attrs={"class": "textinput textInput form-control"}),
    )

    class Meta:
        model = Book
        fields = ["title", "genre", "author", "rating"]

    @staticmethod
    def filter_by_order(queryset, name, value):
        expression = "price" if value == "ascending" else "-price"
        return queryset.order_by(expression)


# own filters
def filter_rating(min_rating, max_rating):
    if min_rating and not max_rating:
        context = Book.objects.filter(rating__gte=min_rating)
    elif max_rating and not min_rating:
        context = Book.objects.filter(rating__lte=max_rating)
    else:
        context = Book.objects.filter(rating__gte=min_rating, rating__lte=max_rating)
    return context


def filter_books(
    genre: str = None,
    title: str = None,
    author: str = None,
    max_rating: str = None,
    min_rating: str = None,
):
    context = Book.objects.none()
    if author:
        first_name = author.split(" ")[0]
        last_name = author.split(" ")[1]
        author = Author.objects.get(first_name=first_name, last_name=last_name)
    if genre:
        genre = Genre.objects.get(name=genre)

    if any([genre, title, author, max_rating, min_rating]):
        if all([genre, title, author, max_rating, min_rating]):
            context = Book.objects.filter(
                title__icontains=title, genre=genre, authors=author
            )
            context = context.filter(rating__gte=min_rating, rating__lte=max_rating)

        elif genre:
            context = Book.objects.filter(genre=genre)

        elif title:
            context = Book.objects.filter(title__icontains=title)

        elif author:
            context = Book.objects.filter(authors=author)

        elif min_rating or max_rating:
            return filter_rating(min_rating, max_rating)

    if len(context.all()) == 0:
        return Book.objects.none()

    return context
