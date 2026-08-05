from pages.registration_page import Registration
from faker import Faker


def test_registration(browser, base_url):
    page = Registration(browser, base_url)
    page.open()
    assert page.title().is_displayed()
    page.input_password("123")
    assert page.password_value() == "123"
    assert "Enter a password between 8 and 72 characters" in page.password_length_hint()
    assert "The minimum score must be: Strong" in page.password_score_hint()
    page.click_save()
    assert (
        page.firstname_field().get_attribute("validationMessage")
        == "Заполните это поле."
    )
    page.send_first_name(Faker().first_name())
    page.send_last_name(Faker().last_name())
    page.input_password(Faker().password())
    page.send_email(Faker().email())
    page.click_check_agree()
    page.click_check_privacy()
    page.click_save()
    assert page.logout_button().is_displayed()
