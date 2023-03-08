from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from app.models import Specialist, City


SPECIALISTS_COUNT = 20


class IndexView(View):
    """Главная страница."""

    def get(self, request: HttpRequest):
        """Получение главной страницы."""
        specialists = Specialist.objects.filter(on_main=True)[:SPECIALISTS_COUNT]
        cities = City.objects.filter(is_active=True)

        context = {"specialists": specialists, "promotions": [], "cities": cities}
        return render(request, "index.html", context)
