from abc import ABC, abstractmethod
from typing import Any


class ICacheRepository(ABC):
    @abstractmethod
    def save_in_cache(self, key: str, value: Any, time: int):
        pass

    @abstractmethod
    def get_from_cache(self, key: str) -> Any:
        pass
