from pydantic import BaseModel

from src.core.validator.state.enum.country.enum import Country


class StateParams(BaseModel):
    country: Country
