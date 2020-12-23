from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from books.api.api_views import AuthorViewSet, BookViewSet, GenreViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"genres", GenreViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
