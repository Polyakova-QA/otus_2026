def get_customer(connection, customer_id: int) -> dict | None:
    sql = "SELECT * FROM ps_customer WHERE id_customer = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        return cursor.fetchone()


def create_customer(connection, customer_data: dict) -> int:
    sql = (
        "INSERT INTO ps_customer "
        "(id_gender, firstname, lastname, email, passwd, date_add, date_upd) "
        "VALUES (%(id_gender)s, %(firstname)s, %(lastname)s, %(email)s, "
        "%(passwd)s, NOW(), NOW())"
    )
    with connection.cursor() as cursor:
        cursor.execute(sql, customer_data)
        return cursor.lastrowid


def update_customer(connection, customer_id: int, customer_data: dict) -> int:
    sql = (
        "UPDATE ps_customer SET firstname = %(firstname)s, "
        "lastname = %(lastname)s, email = %(email)s, date_upd = NOW() "
        "WHERE id_customer = %(id_customer)s"
    )
    with connection.cursor() as cursor:
        cursor.execute(sql, {**customer_data, "id_customer": customer_id})
        return cursor.rowcount


def delete_customer(connection, customer_id: int) -> int:
    sql = "DELETE FROM ps_customer WHERE id_customer = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        return cursor.rowcount
