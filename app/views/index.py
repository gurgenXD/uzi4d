from django.shortcuts import render
from django.utils import timezone
from django.views import View

from app.models import City, Promotion, Rating, Specialist


SPECIALISTS_COUNT = 20


class IndexView(View):
    """Главная страница."""

    def get(self, request):
        """Получение главной страницы."""
        specialists = Specialist.objects.filter(on_main=True)[:SPECIALISTS_COUNT]
        cities = City.objects.filter(is_active=True)
        promotions = Promotion.objects.filter(on_main=True, date_end__gte=timezone.now())
        ratings = Rating.objects.all()

        context = {
            "specialists": specialists,
            "promotions": promotions,
            "cities": cities,
            "ratings": ratings,
        }
        return render(request, "index.html", context)
