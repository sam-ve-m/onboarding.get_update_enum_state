from pydantic import BaseModel

from src.core.validator.country_enum import Country


class StateParams(BaseModel):
    country: Country
