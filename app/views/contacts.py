from django.shortcuts import render
from django.views import View

from app.models import City


class ContactsView(View):
    """Страница контактов."""

    def get(self, request):
        """Получение страницы контактов."""
        cities = City.objects.filter(is_active=True)

        context = {"cities": cities}
        return render(request, "contacts.html", context)
