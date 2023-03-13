from django.shortcuts import render
from django.views import View

from app.models import DocumentCategory, License


class DocumentsView(View):
    """Страница документов."""

    def get(self, request):
        """Получение страницы документов."""
        documents_categories = DocumentCategory.objects.all()
        licenses = License.objects.all()

        context = {"documents_categories": documents_categories, "licenses": licenses}
        return render(request, "documents.html", context)
