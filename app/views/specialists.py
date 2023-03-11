from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views import View

from app.forms.specialists import SpecialistsFilterForm
from app.models import Specialist


PER_PAGE = 12


class SpecialistsView(View):
    """Страница специалистов."""

    def get(self, request):
        """Получение специалистов."""
        page_number = request.GET.get("page", 1)

        query = Specialist.objects.filter().order_by("surname")

        form = SpecialistsFilterForm(request.GET)

        if form.is_valid():
            if form.cleaned_data.get("can_online"):
                query = query.filter(can_online=True)

            if form.cleaned_data.get("can_adult"):
                query = query.filter(can_adult=True)

            if form.cleaned_data.get("can_child"):
                query = query.filter(can_child=True)

            if search_query := form.cleaned_data.get("search_query"):
                query = query.filter(
                    Q(name__icontains=search_query) | Q(surname__icontains=search_query)
                )

            if specialization_guid := form.cleaned_data.get("specialization_guid"):
                query = query.filter(specializations__guid=specialization_guid)

        paginator = Paginator(query, PER_PAGE)
        page_obj = paginator.get_page(page_number)

        context = {
            "page_obj": page_obj,
            "specialization_id": None,
            "specializations": [],
            "form": form,
        }
        return render(request, "specialists.html", context)
