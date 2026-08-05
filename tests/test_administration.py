from pages.administration_page import Administration


def test_administration(browser, base_url):
    page: Administration = Administration(browser, base_url).open()
    assert "Email address" in page.email()
    assert "Password" in page.password()

    page.submit()
    error = page.required_error()
    assert error.get_attribute("class") == "help-block"
    assert "This field is required." in error.text

    assert page.check_stay_logged_in()

    page.open_forgot_password()
    text_error = (
        "You can reset your password every 360 minute(s) only. Please try again later."
    )
    assert text_error in page.reset_password("mail@mail.com")