from datetime import date

from pydantic import BaseModel, Field, validator


EMPTY_GUID = "00000000-0000-0000-0000-000000000000"


class SourceSpecialistSchema(BaseModel):
    """Схема специалистов из источника."""

    guid: str = Field(alias="Guid1C")
    name: str = Field(alias="Name")
    surname: str = Field(alias="Surname")
    patronymic: str | None = Field(alias="MiddleName")
    can_adult: bool = Field(alias="ReceptionAdult")
    can_child: bool = Field(alias="ReceptionChild")

    education: str = "education"
    start_work_date: date = Field(default_factory=date.today)
    on_main: bool = False
    is_active: bool = True
    can_online: bool = False


class ServiceSchema(BaseModel):
    """Схема услуги."""

    guid: str = Field(alias="Guid1C")
    parent_id: str = Field(alias="ParentGuid1C")
    name: str = Field(alias="ProductName")

    @validator("parent_id", pre=True)
    @classmethod
    def empty_str_to_none(cls, v):
        """Перевести пустую строку в None."""
        return None if v == EMPTY_GUID else v


class CatalogItemSchema(BaseModel):
    """Схема элемента каталога."""

    guid: str = Field(alias="Guid1C")
    name: str = Field(alias="CatalogName")
    parent_id: str | None = Field(alias="ParentGuid1C")
    services: list[ServiceSchema] = Field(alias="ProductList")

    @validator("parent_id", pre=True)
    @classmethod
    def empty_str_to_none(cls, v):
        """Перевести пустую строку в None."""
        return None if v == EMPTY_GUID else v


class CatalogSchema(BaseModel):
    """Схема каталога."""

    guid: str = Field(alias="Guid1C")
    name: str = Field(alias="CatalogName")
