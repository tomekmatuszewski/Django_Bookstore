from books.models import Book, Author, Genre


def filter_books(genre: str = None, title: str = None, author: str = None, max_rating: str = None, min_rating: str = None):
    context = False
    if author:
        first_name = author.split(' ')[0]
        last_name = author.split(' ')[1]
        author = Author.objects.get(first_name=first_name, last_name=last_name)
    if genre:
        genre = Genre.objects.get(name=genre)

    if all([genre, title, author, max_rating, min_rating]):
        context = Book.objects.filter(title__icontains=title, genre=genre, authors=author)
        context = context.filter(rating__gte=min_rating, rating__lte=max_rating)

    elif genre:
        context = Book.objects.filter(genre=genre)

    elif title:
        context = Book.objects.filter(title__icontains=title)

    elif author:
        context = Book.objects.filter(authors=author)

    elif min_rating and max_rating:
        context = Book.objects.filter(rating__gte=min_rating, rating__lte=max_rating)

    return context
