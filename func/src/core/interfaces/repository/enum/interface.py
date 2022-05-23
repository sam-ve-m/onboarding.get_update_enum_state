from abc import ABC, abstractmethod
from typing import List, Any


class IEnumRepository(ABC):
    @abstractmethod
    def get_enums(self) -> List[Any]:
        pass

    @abstractmethod
    def _get_cached_enum(self, query: str) -> List[Any]:
        pass
