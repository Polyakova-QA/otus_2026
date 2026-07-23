from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


PAGE_WAIT_TIME = 1


def test_main_page(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, PAGE_WAIT_TIME)
    try:
        logo = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#_desktop_logo img"))
        )
    except TimeoutException:
        pytest.fail(f"Сайт не загрузился за {PAGE_WAIT_TIME} секунд")
    assert logo.is_displayed()
    assert browser.title == "PrestaShop"
    cards = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "#content article.product-miniature")
        )
    )
    assert len(cards) > 1
    like = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "#content > section:nth-child(2) > div > div:nth-child(1) > article > div > button > i",
            )
        )
    )
    like.click()
    expected_text = "You need to be logged in to save products in your wishlist."
    modal = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "#footer > div.footer-container > div > div:nth-child(1) > div.wishlist-login > div.wishlist-modal.modal.fade.show > div > div > div.modal-body > p",
            )
        )
    )
    assert expected_text in modal.text
    close = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "#footer > div.footer-container > div > div:nth-child(1) > div.wishlist-login > div.wishlist-modal.modal.fade.show > div > div > div.modal-header > button",
            )
        )
    )
    close.click()
    cards_on_sale = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "#content section:nth-child(5) article.product-miniature")
        )
    )
    assert len(cards_on_sale) > 1
    current_url = browser.current_url
    click_all_new_products = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#content > section:nth-child(6) > a")
        )
    )
    click_all_new_products.click()
    wait.until(EC.url_changes(current_url))
    assert "new-products" in browser.current_url
