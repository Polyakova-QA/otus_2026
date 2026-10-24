import pymysql
import pytest

from helpers.db import create_customer, delete_customer


def pytest_addoption(parser):
    parser.addoption(
        "--host",
        action="store",
        default="localhost",
        help="Адрес сервера для интеграционных тестов",
    )
    parser.addoption(
        "--port",
        action="store",
        type=int,
        default=3306,
        help="Порт сервера для интеграционных тестов",
    )
    parser.addoption(
        "--database",
        action="store",
        default="prestashop",
        help="Имя базы данных для тестов",
    )
    parser.addoption(
        "--user",
        action="store",
        default="root",
        help="Имя пользователя для подключения к БД",
    )
    parser.addoption(
        "--password",
        action="store",
        default="admin",
        help="Пароль для подключения к БД",
    )


@pytest.fixture(scope="session")
def connection(request):
    conn = pymysql.connect(
        host=request.config.getoption("--host"),
        port=int(request.config.getoption("--port")),
        database=request.config.getoption("--database"),
        user=request.config.getoption("--user"),
        password=request.config.getoption("--password"),
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )
    yield conn
    conn.close()


@pytest.fixture
def customer_data():
    return {
        "id_gender": 1,
        "firstname": "Test",
        "lastname": "User",
        "email": "test@example.com",
        "passwd": "test_password",
    }


@pytest.fixture
def customer(connection, customer_data):
    customer_id = create_customer(connection, customer_data)
    yield customer_id
    delete_customer(connection, customer_id)
