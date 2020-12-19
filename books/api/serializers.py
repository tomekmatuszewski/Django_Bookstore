from rest_framework.serializers import ModelSerializer

from books.models import Author, Book, Genre


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class BookSerializer(ModelSerializer):

    authors = AuthorSerializer(many=True)
    genre = GenreSerializer()

    class Meta:
        model = Book
        fields = "__all__"


class BookMiniSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title']
