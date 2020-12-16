from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):

    template_name = "home.html"
    extra_context = {"title": "Home"}


