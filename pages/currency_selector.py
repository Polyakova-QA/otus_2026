import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import CurrencySelectorLocators


class CurrencySelector(BasePage):
    @allure.step("Получить цену")
    def price(self):
        return self.find(CurrencySelectorLocators.PRICE).text

    @allure.step("Переключить валюту на USD")
    def switch_to_usd(self):
        self.click(CurrencySelectorLocators.TOGGLE)
        self.wait.until(
            EC.element_to_be_clickable(CurrencySelectorLocators.USD_OPTION)
        ).click()
        return self
