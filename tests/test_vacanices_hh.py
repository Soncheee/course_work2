import pytest
from src.vacancies_hh import Vacancies

def test_initialization_and_properties():
    vac = Vacancies("Test Job", "http://example.com", 5000, "Description here")
    assert vac.name == "Test Job"
    assert vac.url == "http://example.com"
    assert vac.payment == 5000
    assert vac.description == "Description here"

def test_validation_payment_none():
    vac = Vacancies("Test Job", "http://example.com", None, "Desc")
    assert vac.payment == 0

def test_comparison_operators():
    vac1 = Vacancies("Job1", "url1", 3000, "")
    vac2 = Vacancies("Job2", "url2", 5000, "")
    vac3 = Vacancies("Job3", "url3", 5000, "")

    assert vac1 < vac2
    assert vac2 > vac1
    assert vac2 == vac3
