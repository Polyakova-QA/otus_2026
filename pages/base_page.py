from abc import ABC

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators import HeaderLocators
from utils.logger import setup_logger


class BasePage(ABC):
    PATH = ""

    def __init__(self, browser, timeout=4):
        self.browser = browser
        self.base_url = browser.base_url
        self.wait = WebDriverWait(browser, timeout)
        self.logger = setup_logger(type(self).__name__)

    @allure.step("Открыть страницу")
    def open(self, path=None):
        target = self.PATH if path is None else path
        url = self.base_url + target
        self.logger.info("Открываю %s", url)
        self.browser.get(url)
        return self

    def find(self, locator):
        self.logger.info("Ищу элемент %s", locator)
        try:
            return self.browser.find_element(*locator)
        except Exception as error:
            self.logger.exception("Не удалось найти элемент %s: %s", locator, error)
            raise

    def find_all(self, locator):
        return self.browser.find_elements(*locator)

    def click(self, locator):
        self.logger.info("Кликаю %s", locator)
        try:
            self.find(locator).click()
        except Exception as error:
            self.logger.exception("Не удалось кликнуть по %s: %s", locator, error)
            raise

    def js_click(self, locator):
        self.browser.execute_script("arguments[0].click();", self.find(locator))

    def wait_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as error:
            self.logger.exception("Элемент %s не стал видимым: %s", locator, error)
            raise

    def current_url(self):
        return self.browser.current_url

    def wait_url_changes(self, current_url):
        self.wait.until(EC.url_changes(current_url))

    @allure.step("Получить имя пользователя в шапке")
    def account_name(self):
        return self.wait_visible(HeaderLocators.ACCOUNT_NAME).text

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(HeaderLocators.LOGOUT)
        return self.find(HeaderLocators.SIGN_IN).text

    def logout_button(self):
        return self.wait_visible(HeaderLocators.LOGOUT)

    def hide_debug_toolbar(self):
        self.browser.execute_script(
            "document.querySelectorAll('.sf-toolbar, .sf-minitoolbar')"
            ".forEach(function(t){ t.style.display = 'none'; });"
        )
        return self
