from django import forms

from app.models import Specialization


class SpecialistsFilterForm(forms.Form):
    """Форма фильтрации специалистов."""

    can_online = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input", "id": "HasOnline"}),
    )
    can_adult = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input", "id": "HasAdult"}),
    )
    can_child = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input", "id": "HasChild"}),
    )
    search_query = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "SpecialitName",
                "placeholder": "Фамилия или имя врача",
            }
        ),
    )
    specialization_guid = forms.ModelChoiceField(
        queryset=Specialization.objects.all(),
        empty_label="Все специальности",
        initial=0,
        required=False,
        widget=forms.Select(attrs={"class": "form-select", "id": "SpecializationID"}),
    )
