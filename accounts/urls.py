from django.urls import path
from accounts.views import SignUpView, MyLoginView, PasswordChangeViewOwn
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('bookstore/sign-up', SignUpView.as_view(), name="signup"),
    path('bookstore/log-in', MyLoginView.as_view(), name="login"),
    path('bookstore/password-change', PasswordChangeViewOwn.as_view(), name="password-change"),
    path('bookstore/log-out', LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),

]