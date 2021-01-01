from django_filters import rest_framework as filters

from books.models import Book


class BookApiFilter(filters.FilterSet):

    CHOICES = (("ascending", "ascending"), ("descending", "descending"))

    title = filters.CharFilter(
        field_name="title", lookup_expr="icontains", label="title"
    )
    genre = filters.CharFilter(
        field_name="genre__name", lookup_expr="icontains", label="genre"
    )
    author = filters.CharFilter(
        field_name="authors", method="filter_by_author", label="author"
    )

    rating = filters.RangeFilter(label="Rating Between", field_name="rating")

    ordering = filters.ChoiceFilter(
        label="Ordering by Price", choices=CHOICES, method="filter_by_order"
    )

    class Meta:
        model = Book
        fields = ["title", "genre"]

    @staticmethod
    def filter_by_order(queryset, name, value):
        expression = "price" if value == "ascending" else "-price"
        return queryset.order_by(expression)

    @staticmethod
    def filter_by_author(queryset, name, value):
        if " " in value:
            full_name = value.split(" ")
            first_name = full_name[0].title()

            last_name = full_name[1].title()
            fullname = queryset.filter(authors__first_name=first_name).filter(
                authors__last_name=last_name
            )
        else:
            return queryset.filter(
                authors__first_name=value.title()
            ) or queryset.filter(authors__last_name=value.title())

        return fullname
