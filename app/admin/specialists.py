from django.contrib import admin

from app.models import Specialist, Specialization


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    """Специализации в админ-панели."""

    list_display = ("guid", "name")

    # def has_change_permission(
    # ):
    #     """Права на изменение."""

    # def has_add_permission(self, _request):
    #     """Права на добавление."""

    # def has_delete_permission(
    # ):
    #     """Права на удаление."""


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    """Специалисты в админ-панели."""

    list_display = ("surname", "name", "patronymic", "on_main", "is_active")

    def has_change_permission(self, _request, _obj=None):
        """Права на изменение."""
        return False

    def has_add_permission(self, _request):
        """Права на добавление."""
        return False

    def has_delete_permission(self, _request, _obj=None):
        """Права на удаление."""
        return False
