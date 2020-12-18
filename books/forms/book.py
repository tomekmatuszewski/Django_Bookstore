from django.forms import DecimalField, ImageField, ModelForm, ModelMultipleChoiceField

from books.models import Author, Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    rating = DecimalField(decimal_places=1, min_value=1.0, max_value=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if isinstance(visible.field, ImageField):
                pass
            else:
                visible.field.widget.attrs["class"] = "form-control"
