import os
from pages.login_page import LoginPage


def test_authorization(browser):
    page = LoginPage(browser).open()
    page.login("mail@mail.com", os.getenv("TEST_PASSWORD"))
    assert page.account_name() == "Nadezhda P."
    assert page.logout() == "Sign in"
