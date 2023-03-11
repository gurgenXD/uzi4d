from django.contrib import admin

from app.models import Document, DocumentCategory


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    """Категории документов в админ-панели."""


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """Документы в админ-панели."""
