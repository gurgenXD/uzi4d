from django.contrib import admin

from updater.models import Updater
from admin_extra_buttons.api import ExtraButtonsMixin, button
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from updater.service import update_all


@admin.register(Updater)
class UpdaterAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ("id", "start_update", "end_update", "status")

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @button(html_attrs={"style": "background-color:#DC6C6C;color:black"})
    def update(self, request):
        update_all(host="http://195.2.192.1:8880/4d_portalz_08/hs/site/v1")

        return HttpResponseRedirectToReferrer(request)
