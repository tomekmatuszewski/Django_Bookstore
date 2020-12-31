from django_filters import rest_framework as filters
from books.models import Book


class BookApiFilter(filters.FilterSet):

    title = filters.CharFilter(field_name='title', lookup_expr='icontains', label='title')
    genre = filters.CharFilter(field_name='genre__name', lookup_expr='icontains', label='genre')

    class Meta:
        model = Book
        fields = ['title', 'genre']
