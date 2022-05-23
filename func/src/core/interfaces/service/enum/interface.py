from abc import ABC, abstractmethod


class IEnumService(ABC):
    @abstractmethod
    def get_response(self):
        pass
