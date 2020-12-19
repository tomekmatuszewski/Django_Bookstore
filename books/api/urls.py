from django.urls import include, path
from rest_framework.routers import DefaultRouter

from books.api.api_views import AuthorViewSet, BookViewSet, GenreViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"genres", GenreViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
