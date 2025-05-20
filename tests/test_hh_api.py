import pytest
from src.hh_api import HH_API


def test_load_vacancies_real_api():
    api = HH_API()
    results = api.load_vacancies('Python')

    assert isinstance(results, list)
    if results:
        first_vacancy = results[0]
        assert 'name' in first_vacancy
        assert 'url' in first_vacancy
        assert 'payment' in first_vacancy
        assert 'description' in first_vacancy