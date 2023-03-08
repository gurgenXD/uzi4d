from datetime import date
from pydantic import BaseModel, validator, Field


class SourceSpecialistSchema:
    id: str = Field(alias="Guid1C")
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


class SourceServiceGroupSchema(BaseModel):
    """Схема группы услуг из источника."""

    id: str = Field(alias="Guid1C")
    parent_id: str | None = Field(alias="ParentGuid1C")
    name: str = Field(alias="GroupName")
    level: int = Field(alias="GroupLevel")

    on_main: bool = False
    is_active: bool = True
    is_group: bool = True

    @validator("parent_id", pre=True)
    @classmethod
    def empty_str_to_none(cls, v: str | None) -> str | None:
        """Перевести пустую строку в None."""
        if v == "":
            return None
        return v


class SourceServiceSchema(BaseModel):
    """Схема услуги из источника."""

    id: str = Field(alias="Guid1C")
    parent_id: str | None = Field(alias="ParentGuid1C")
    name: str = Field(alias="ProductName")
    level: int = Field(alias="ProductLevel")

    on_main: bool = False
    is_active: bool = True
    is_group: bool = False

    @validator("parent_id", pre=True)
    @classmethod
    def empty_str_to_none(cls, v: str | None) -> str | None:
        """Перевести пустую строку в None."""
        if v == "":
            return None
        return v
