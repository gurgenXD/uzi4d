from django.shortcuts import render
from django.utils import timezone
from django.views import View

from app.models import Promotion


class PromotionsView(View):
    """Страница спецпредложений."""

    def get(self, request):
        """Получение страницы спецпредложений."""
        promotions = Promotion.objects.filter(date_end__gte=timezone.now())

        context = {"promotions": promotions}
        return render(request, "promotions.html", context)
