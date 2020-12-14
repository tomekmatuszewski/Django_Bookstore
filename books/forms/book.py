from django.forms import ModelForm
from books.models import Book, Author
from django.forms import IntegerField, ModelMultipleChoiceField, ImageField


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    rating = IntegerField(min_value=1, max_value=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if isinstance(visible.field, ImageField):
                pass
            else:
                visible.field.widget.attrs['class'] = 'form-control'
