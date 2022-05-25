from src.repository.enum.repository import EnumRepository
from src.repository.base_repository.cache.repository import CacheRepository
from src.repository.base_repository.oracle.repository import OracleBaseRepository
from tests.test_doubles.doubles import (
    enum_repository_get_cached_enum_dummy,
    enum_repository_get_from_cache_dummy_none,
    enum_repository_get_from_cache_dummy_list,
    enum_repository_query_dummy,
    enum_repository_save_in_cache_dummy,
)
from unittest.mock import patch


@patch.object(EnumRepository, "_get_cached_enum")
def test_get_enums(_get_cached_enum_mock):
    _get_cached_enum_mock.return_value = enum_repository_get_cached_enum_dummy
    result = EnumRepository.get_enums("USA")
    _get_cached_enum_mock.assert_called_with(EnumRepository.enum_query, "USA")
    assert type(result) == list
    for item in result:
        assert type(item) == tuple


@patch.object(OracleBaseRepository, "query")
@patch.object(CacheRepository, "save_in_cache")
@patch.object(CacheRepository, "get_from_cache")
def test_get_cached_enums_when_there_is_cache(
    get_from_cache_mock, save_in_cache_mock, query_mock
):
    get_from_cache_mock.return_value = enum_repository_get_from_cache_dummy_list
    save_in_cache_mock.return_value = enum_repository_query_dummy
    query_mock.return_value = enum_repository_save_in_cache_dummy

    result = EnumRepository._get_cached_enum(EnumRepository.enum_query, "USA")

    query_mock.assert_not_called()
    save_in_cache_mock.assert_not_called()
    get_from_cache_mock.assert_called_with(EnumRepository.enum_key.format("USA"))
    assert result == CacheRepository.get_from_cache("")


@patch.object(OracleBaseRepository, "query")
@patch.object(CacheRepository, "save_in_cache")
@patch.object(CacheRepository, "get_from_cache")
def test_get_cached_enums_when_there_is_no_cache(
    get_from_cache_mock, save_in_cache_mock, query_mock
):
    get_from_cache_mock.return_value = enum_repository_get_from_cache_dummy_none
    save_in_cache_mock.return_value = enum_repository_query_dummy
    query_mock.return_value = enum_repository_save_in_cache_dummy

    result = EnumRepository._get_cached_enum(EnumRepository.enum_query, "USA")

    query_mock.assert_called_with(sql=EnumRepository.enum_query.format("USA"))
    assert result == OracleBaseRepository.query("USA")
    assert save_in_cache_mock.called
