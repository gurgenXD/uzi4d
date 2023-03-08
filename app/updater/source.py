from dataclasses import dataclass

import requests

from updater.schemas import SourceServiceGroupSchema, SourceServiceSchema, SourceSpecialistSchema


@dataclass
class SourceAdapter:
    _host: str
    _timeout: int = 60

    def get_specialists(self) -> list["SourceSpecialistSchema"]:
        response = requests.get(f"{self._host}/doctor/GetDoctorList", timeout=self._timeout)
        return [SourceSpecialistSchema(**item) for item in response.json()]

    def get_services_groups(self) -> list["SourceServiceGroupSchema"]:
        response = requests.get(f"{self._host}/product/GetProductGroups", timeout=self._timeout)
        return [SourceServiceGroupSchema(**item) for item in response.json()]

    def get_services(self) -> list["SourceServiceSchema"]:
        response = requests.get(f"{self._host}/product/GetExtProductList", timeout=self._timeout)
        return [SourceServiceSchema(**item) for item in response.json()]
