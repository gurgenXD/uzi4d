from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from app.models import Specialist


SPECIALISTS_COUNT = 20


class IndexView(View):
    """Главная страница."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Получение главной страницы."""
        specialists = Specialist.objects.filter(on_main=True)[:SPECIALISTS_COUNT]

        context = {"specialists": specialists, "promotions": [], "cities": []}
        return render(request, "index.html", context)
