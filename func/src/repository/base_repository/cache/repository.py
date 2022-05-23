from typing import Union

from mnemosine import SyncCache

from src.core.interfaces.repository.cache.interface import ICacheRepository


class CacheRepository(ICacheRepository):
    @classmethod
    def save_in_cache(cls, key: str, value: list, time: int = 3600) -> bool:
        try:
            SyncCache.save(str(key), list(value), int(time))
            return True
        except ValueError:
            return False
        except TypeError:
            return False

    @classmethod
    def get_from_cache(cls, key: str) -> Union[list, None]:
        result = SyncCache.get(key)
        return result
