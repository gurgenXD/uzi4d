"""app URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/

Examples
--------
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app.views import (
    ContactsView,
    DocumentsView,
    IndexView,
    PromotionsView,
    ServicesView,
    ServiceView,
    SpecialistsView,
    SpecialistView,
)


admin.site.site_header = "Поликлиника УЗИ-4D"


urlpatterns = [
    # Админ панель.
    path("admin/", admin.site.urls),
    # URL приложения.
    path("", IndexView.as_view(), name="index"),
    path("specialists/", SpecialistsView.as_view(), name="specialists"),
    path("specialists/<guid>", SpecialistView.as_view(), name="specialist"),
    path("services/", ServicesView.as_view(), name="services"),
    path("services/<guid>", ServiceView.as_view(), name="service"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("documents/", DocumentsView.as_view(), name="documents"),
    path("promotions/", PromotionsView.as_view(), name="promotions"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
