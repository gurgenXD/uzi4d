from django.shortcuts import render
from django.views import View
from app.models import Specialist
from django.http import HttpRequest, HttpResponse

SPECIALISTS_COUNT = 20


class SpecialistsView(View):
    """Страница специалистов."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Получение специалистов."""
        specialists = Specialist.objects.filter(on_main=True)[:SPECIALISTS_COUNT]

        context = {"specialists": specialists, "promotions": [], "cities": []}
        return render(request, "specialists.html", context)
