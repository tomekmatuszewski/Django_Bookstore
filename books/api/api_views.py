from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from books.models import Author, Book, Genre

from .serializers import (AuthorSerializer, BookMiniSerializer, BookSerializer,
                          GenreSerializer)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "genre__name", "authors__last_name"]

    @action(detail=True, methods=["POST"])
    def stock(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.in_stock = request.data.get("in_stock")
        instance.save()
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        serializer = BookMiniSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
