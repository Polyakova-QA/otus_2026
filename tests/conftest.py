import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru", help="URL для проверки")
    parser.addoption("--status_code", default=200, help="Ожидаемый статус-код")


@pytest.fixture(scope="session")
def url(pytestconfig):
    return pytestconfig.getoption("--url")


@pytest.fixture(scope="session")
def status_code(pytestconfig):
    return int(pytestconfig.getoption("--status_code"))
