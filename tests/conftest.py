import pytest


@pytest.fixture(scope="session", autouse=True)
def start_bd():
    pass

    yield

    pass
