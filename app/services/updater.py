import traceback

from django.utils import timezone

from app.models import (
    Service,
    ServiceCatalog,
    ServiceCategory,
    Specialist,
    Updater,
    UpdaterStatusType,
)
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
        ServiceCategory.objects.all().delete()
        ServiceCatalog.objects.all().delete()

        for catalog in source.get_catalogs():
            catalog_model = ServiceCatalog(**catalog.dict())
            catalog_model.save()

            for category in source.get_catalog_content(guid=catalog.guid):
                category_model = ServiceCategory(
                    **category.dict(exclude={"services"}), catalog=catalog_model
                )
                category_model.save()

                for service in category.services:
                    service_model = Service(**service.dict(exclude={"parent_id"}))
                    service_model.save()

                    category_model.services.add(service_model)
    except Exception:  # noqa: BLE001
        status = UpdaterStatusType.FAILURE.value
        message = str(traceback.format_exc())

    updater.status = status
    updater.error_log = message
    updater.end_update = timezone.now()
    updater.save()
