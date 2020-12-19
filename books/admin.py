from django.contrib import admin
from django.contrib.admin import ModelAdmin

from books.models import Author, Book, Genre


class BookAdmin(ModelAdmin):
    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ["title"]
    list_display = [
        "id",
        "title",
        "price",
        "image",
        "publication_year",
        "description",
        "rating",
        "genre",
    ]
    list_display_links = ["id", "title"]
    list_per_page = 10
    list_filter = ["genre", "authors"]
    search_fields = ["title"]
    actions = ["cleanup_description"]

    fieldsets = [
        (None, {"fields": ["title", "image"]}),
        (
            "External Information",
            {
                "fields": ["genre", "publication_year", "authors"],
                "description": (
                    "These fields are going to be filled with data parsed "
                    "from external databases."
                ),
            },
        ),
        (
            "User Information",
            {
                "fields": ["rating", "description", "price"],
                "description": "These fields are intended to be filled in by our users.",
            },
        ),
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Author)
