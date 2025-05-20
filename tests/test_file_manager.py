import pytest
import os
from src.vacancies_hh import Vacancies
from src.file_manager import JsonFile

TEST_FILE = 'tests/test_data.json'


@pytest.fixture(autouse=True)
def cleanup():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_add_and_get_vacancy():
    fm = JsonFile(TEST_FILE)
    vac = Vacancies("Test Job", "http://example.com", 4000, "Desc")

    fm.add_vacancy(vac)

    vacancies = fm.get_vacancy()
    assert len(vacancies) == 1
    assert vacancies[0].name == "Test Job"


def test_delete_vacancy():
    fm = JsonFile(TEST_FILE)

    vac1 = Vacancies("Job1", "url1", 3000, "")
    vac2 = Vacancies("Job2", "url2", 4000, "")

    fm.add_vacancy(vac1)
    fm.add_vacancy(vac2)

    fm.delete_vacancy(vac1)

    vacancies = fm.get_vacancy()
    names = [v.name for v in vacancies]

    assert "Job1" not in names
    assert "Job2" in names