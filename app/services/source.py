from dataclasses import dataclass

import requests

from app.services.schemas import CatalogItemSchema, SourceSpecialistSchema


@dataclass
class SourceAdapter:
    """Адаптер источника данных."""

    _host: str
    _timeout: int = 60

    def get_specialists(self):
        """Получить специалистов."""
        response = requests.get(f"{self._host}/doctor/GetDoctorList", timeout=self._timeout)
        return [SourceSpecialistSchema(**item) for item in response.json()]

    def get_catalog_content(self, guid):
        """Получить содержимое каталога."""
        response = requests.get(
            f"{self._host}/product/GetCatalogContentByID",
            params={"CatalogID": guid},
            timeout=self._timeout,
        )

        return [CatalogItemSchema(**content) for content in response.json()]
