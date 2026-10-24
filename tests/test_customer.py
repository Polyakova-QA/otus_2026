from helpers.db import delete_customer, get_customer, update_customer

NEW_DATA = {
    "firstname": "NewFirstname",
    "lastname": "NewLastname",
    "email": "new@example.com",
}


def test_create_customer(connection, customer, customer_data):
    created = get_customer(connection, customer)
    assert created is not None
    assert created["firstname"] == customer_data["firstname"]
    assert created["lastname"] == customer_data["lastname"]
    assert created["email"] == customer_data["email"]


def test_update_customer(connection, customer):
    updated = update_customer(connection, customer, NEW_DATA)
    assert updated == 1
    updated_customer = get_customer(connection, customer)
    assert updated_customer["firstname"] == NEW_DATA["firstname"]
    assert updated_customer["lastname"] == NEW_DATA["lastname"]
    assert updated_customer["email"] == NEW_DATA["email"]


def test_update_nonexistent_customer(connection):
    assert get_customer(connection, 9898) is None
    assert update_customer(connection, 9898, NEW_DATA) == 0


def test_delete_customer(connection, customer):
    deleted = delete_customer(connection, customer)
    assert deleted == 1
    assert get_customer(connection, customer) is None


def test_delete_nonexistent_customer(connection):
    assert get_customer(connection, 988900) is None
    deleted = delete_customer(connection, 988900)
    assert get_customer(connection, 988900) is None
    assert deleted == 0
