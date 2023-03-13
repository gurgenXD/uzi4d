from django.contrib import admin

from app.models import Document, DocumentCategory, License


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    """Категории документов в админ-панели."""


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """Документы в админ-панели."""


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    """Лицензии в админ-панели."""

    list_display = ("name", "number")
