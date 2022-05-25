from typing import List, Tuple

from src.core.interfaces.repository.enum.interface import IEnumRepository
from src.repository.base_repository.cache.repository import CacheRepository
from src.repository.base_repository.oracle.repository import OracleBaseRepository


class EnumRepository(IEnumRepository):

    database = OracleBaseRepository
    cache_database = CacheRepository

    enum_query = """
            SELECT SG_ESTADO as initials, NM_ESTADO as description
            FROM CORRWIN.TSCESTADO
            WHERE SG_PAIS='{}'
        """
    enum_key = "EnumState{}"

    @classmethod
    def get_enums(cls, country: str) -> List[Tuple]:
        sql = cls.enum_query
        result = cls._get_cached_enum(sql, country)
        return result

    @classmethod
    def _get_cached_enum(cls, query: str, country: str) -> List[Tuple]:
        if cached_enum := cls.cache_database.get_from_cache(
            cls.enum_key.format(country)
        ):
            return cached_enum

        query = query.format(country)
        enum_values = cls.database.query(sql=query)
        cls.cache_database.save_in_cache(cls.enum_key.format(country), enum_values)
        return enum_values
