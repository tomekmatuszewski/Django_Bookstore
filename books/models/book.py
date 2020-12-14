from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="book_pics", default="default.png", help_text="Min. size 300x300")
    publication_year = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, related_name='genre')
    author = models.ManyToManyField(Author, related_name='authors')

    def __str__(self):
        return self.title
