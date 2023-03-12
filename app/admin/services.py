from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from app.models import Service, ServiceCatalog, ServiceCategory


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Услуги в админ-панели."""

    list_display = ("name", "guid")
    search_fields = ("name", "guid")
    list_filter = ("categories__catalog__name", "categories__name")

    def has_change_permission(self, _request, _obj=None):
        """Права на изменение."""
        return False

    def has_add_permission(self, _request):
        """Права на добавление."""

    def has_delete_permission(self, _request, _obj=None):
        """Права на удаление."""


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(DjangoMpttAdmin):
    """Категории услуг в админ-панели."""

    list_display = ("name", "guid", "parent_id", "catalog")
    list_filter = ("catalog__name",)

    def has_change_permission(self, _request, _obj=None):
        """Права на изменение."""
        return False

    def has_add_permission(self, _request):
        """Права на добавление."""
        return False

    def has_delete_permission(self, _request, _obj=None):
        """Права на удаление."""
        return False


@admin.register(ServiceCatalog)
class ServiceCatalogAdmin(admin.ModelAdmin):
    """Каталог услуг в админ-панели."""

    list_display = ("name", "guid")

    def has_change_permission(self, _request, _obj=None):
        """Права на изменение."""
        return False

    def has_add_permission(self, _request):
        """Права на добавление."""
        return False

    def has_delete_permission(self, _request, _obj=None):
        """Права на удаление."""
        return False
