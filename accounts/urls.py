from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import (MyLoginView, PasswordChangeViewOwn, SignUpView,
                            UserDeleteView, UserUpdateView)

urlpatterns = [
    path("bookstore/sign-up/", SignUpView.as_view(), name="signup"),
    path("bookstore/log-in/", MyLoginView.as_view(), name="login"),
    path(
        "bookstore/password-change/",
        PasswordChangeViewOwn.as_view(),
        name="password-change",
    ),
    path(
        "bookstore/log-out/",
        LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
    path(
        "bookstore/account/<int:pk>/update",
        UserUpdateView.as_view(),
        name="user-update",
    ),
    path(
        "bookstore/account/<int:pk>/delete",
        UserDeleteView.as_view(),
        name="user-delete",
    ),
]
