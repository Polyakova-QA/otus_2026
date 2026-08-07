from abc import ABC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import HeaderLocators


class BasePage(ABC):
    PATH = ""

    def __init__(self, browser, timeout=4):
        self.browser = browser
        self.base_url = browser.base_url
        self.wait = WebDriverWait(browser, timeout)

    def open(self, path=None):
        target = self.PATH if path is None else path
        self.browser.get(self.base_url + target)
        return self

    def find(self, locator):
        return self.browser.find_element(*locator)

    def find_all(self, locator):
        return self.browser.find_elements(*locator)

    def click(self, locator):
        self.find(locator).click()

    def js_click(self, locator):
        # клик через JS — в обход элементов, перекрывающих цель (напр. Symfony WDT)
        self.browser.execute_script("arguments[0].click();", self.find(locator))

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def current_url(self):
        return self.browser.current_url

    def wait_url_changes(self, current_url):
        self.wait.until(EC.url_changes(current_url))

    def account_name(self):
        return self.wait_visible(HeaderLocators.ACCOUNT_NAME).text

    def logout(self):
        self.click(HeaderLocators.LOGOUT)
        return self.find(HeaderLocators.SIGN_IN).text

    def logout_button(self):
        return self.wait_visible(HeaderLocators.LOGOUT)

    def hide_debug_toolbar(self):
        # Symfony WDT состоит из нескольких блоков (полная и мини-панель) —
        # прячем все, чтобы они не перехватывали клики
        self.browser.execute_script(
            "document.querySelectorAll('.sf-toolbar, .sf-minitoolbar')"
            ".forEach(function(t){ t.style.display = 'none'; });"
        )
        return self
