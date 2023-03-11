from django.shortcuts import get_object_or_404, render
from django.views import View

from app.models import Service


class ServicesView(View):
    """Страница услуг."""

    def get(self, request):
        """Получение услуг."""
        services = Service.objects.filter(is_active=True)

        context = {"services": services}
        return render(request, "services.html", context)


class ServiceView(View):
    """Страница услуги."""

    def get(self, request, guid):
        """Получение услуги."""
        service = get_object_or_404(Service, guid=guid, is_active=True)

        context = {"service": service}
        return render(request, "service.html", context)
