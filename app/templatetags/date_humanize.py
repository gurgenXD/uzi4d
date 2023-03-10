from datetime import datetime, timezone

from django import template


register = template.Library()


@register.filter
def calculate_ages(start_date):
    """Посчитать пройденные года."""
    today = datetime.now(tz=timezone.utc).date()
    return today.year - start_date.year


@register.filter
def humanize_age(age):
    """Очеловечивание возраста."""
    if age % 100 in (11, 12, 13, 14):
        return f"{age} лет"

    if age % 10 == 1:
        return f"{age} год"

    if age % 10 in (2, 3, 4):
        return f"{age} года"

    return f"{age} лет"
