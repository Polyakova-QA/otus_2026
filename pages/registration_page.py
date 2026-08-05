from pages.base_page import BasePage
from pages.locators import RegistrationLocators


class Registration(BasePage):
    PATH = "registration"

    def open(self, path=PATH):
        return super().open(path)

    def title(self):
        return self.find(RegistrationLocators.TITLE)

    def input_password(self, password):
        self.find(RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        self.find(RegistrationLocators.SHOW_PASSWORD_BTN).click()
        return self

    def password_value(self):
        return self.find(RegistrationLocators.PASSWORD_INPUT).get_attribute("value")

    def password_length_hint(self):
        return self.find(RegistrationLocators.PASSWORD_LENGTH_HINT).get_attribute(
            "textContent"
        )

    def password_score_hint(self):
        return self.find(RegistrationLocators.PASSWORD_SCORE_HINT).get_attribute(
            "textContent"
        )

    def click_save(self):
        self.find(RegistrationLocators.SUBMIT).click()
        return self

    def firstname_field(self):
        return self.find(RegistrationLocators.FIRSTNAME)

    def send_first_name(self, first_name):
        self.find(RegistrationLocators.FIRSTNAME).send_keys(first_name)

    def send_last_name(self, last_name):
        self.find(RegistrationLocators.LASTNAME).send_keys(last_name)

    def click_check_agree(self):
        self.find(RegistrationLocators.CHECK_AGREE).click()
        return self

    def click_check_privacy(self):
        self.find(RegistrationLocators.CHECK_PRIVACY).click()
        return self

    def send_email(self, email):
        self.find(RegistrationLocators.EMAIL).send_keys(email)
