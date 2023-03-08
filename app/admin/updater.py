from admin_extra_buttons.api import ExtraButtonsMixin, button
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from django.conf import settings
from django.contrib import admin
from django.http import HttpRequest

from app.models import Updater
from app.services.updater import update_all


@admin.register(Updater)
class UpdaterAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    """Обновления в админ-панели."""

    list_display = ("id", "start_update", "end_update", "status")

    def has_change_permission(self, _request: HttpRequest, _obj: Updater | None = None) -> bool:
        """Права на изменение."""
        return False

    def has_add_permission(self, _request: HttpRequest) -> bool:
        """Права на добавление."""
        return False

    def has_delete_permission(self, _request: HttpRequest, _obj: Updater | None = None) -> bool:
        """Права на удаление."""
        return False

    @button(label="Обновить данные", html_attrs={"style": "background-color:#417690"})
    def update(self, request: HttpRequest) -> HttpResponseRedirectToReferrer:
        """Обновить репозиторий."""
        update_all(host=settings.SERVICE_SOURCE_HOST)
        return HttpResponseRedirectToReferrer(request)
