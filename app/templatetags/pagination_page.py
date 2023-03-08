import re

from django import template


register = template.Library()
PAGE_NUMBER_REGEX = re.compile(r"(page=[0-9]*[\&]*)")


@register.filter
def append_page_param(value, page_number=None):
    """Добавление страницы к URL'у."""
    value = re.sub(PAGE_NUMBER_REGEX, "", value)

    if page_number:
        if "?" not in value:
            value += f"?page={page_number}"
        elif value[-1] != "&":
            value += f"&page={page_number}"
        else:
            value += f"page={page_number}"

    return value
