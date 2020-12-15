from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SingUpForm


class SignUpView(CreateView):

    template_name = 'accounts/form.html'
    form_class = SingUpForm
    success_url = reverse_lazy('bookstore')


class MyLoginView(LoginView):
    template_name = 'accounts/form.html'


class PasswordChangeViewOwn(PasswordChangeView):

    template_name = 'accounts/form.html'
    success_url = reverse_lazy("bookstore")