from django.shortcuts import render
from django.views import View

from app.models import DocumentCategory


class DocumentsView(View):
    """Страница документов."""

    def get(self, request):
        """Получение страницы документов."""
        documents_categories = DocumentCategory.objects.all()

        context = {"documents_categories": documents_categories}
        return render(request, "documents.html", context)
