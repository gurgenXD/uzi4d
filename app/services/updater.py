import traceback

from django.utils import timezone

from app.models import Service, Specialist, Updater, UpdaterStatusType
from app.services.source import SourceAdapter


def update_all(host):
    """Обновить репозиторий."""
    source = SourceAdapter(_host=host)

    updater = Updater(start_update=timezone.now(), status=UpdaterStatusType.PROCESSING.value)
    updater.save()

    status = UpdaterStatusType.SUCCESS.value
    message = ""
    try:
        Specialist.objects.all().delete()
        for specialist in source.get_specialists():
            Specialist(**specialist.dict()).save()

        Service.objects.all().delete()
        for group in source.get_catalog_content(guid="5b06b6c4-c0cd-11ed-9688-70cf49616281"):
            Service(**group.dict(exclude={"services"})).save()
            for service in group.services:
                Service(**service.dict()).save()
    except Exception:  # noqa: BLE001
        status = UpdaterStatusType.FAILURE.value
        message = str(traceback.format_exc())

    updater.status = status
    updater.error_log = message
    updater.end_update = timezone.now()
    updater.save()
