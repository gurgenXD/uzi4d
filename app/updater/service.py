import traceback
from specialists.models import Specialist
from updater.models import Updater, UpdaterStatusType
from django.utils import timezone
from updater.source import SourceAdapter


def update_all(host: str) -> None:
    source = SourceAdapter(_host=host)

    updater = Updater(start_update=timezone.now(), status=UpdaterStatusType.PROCESSING).save()

    status = UpdaterStatusType.SUCCESS
    message = None
    try:
        Specialist.objects.bulk_create(
            [Specialist(**specialist.dict()) for specialist in source.get_specialists()]
        )

        # services_groups = source.get_services_groups()
        # self._services.create_or_update_groups(services_groups)

        # services = source.get_services()
        # self._services.create_or_update(services)
    except Exception:
        status = UpdaterStatusType.FAILURE
        message = str(traceback.format_exc())

    updater.status = status
    updater.error_log = message
    updater.save()
