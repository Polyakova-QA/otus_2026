from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import random
from selenium.webdriver.support.ui import WebDriverWait


def test_add_to_card(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 4)
    products = browser.find_elements(
        By.CSS_SELECTOR, "#content article.product-miniature"
    )
    random_index = random.randint(0, len(products) - 1)
    random_product = products[random_index]
    random_product.click()
    browser.find_element(
        By.CSS_SELECTOR,
        "#add-to-cart-or-refresh > div.product-add-to-cart.js-product-add-to-cart > div > div.add > button",
    ).click()
    modal = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#myModalLabel"))
    )
    assert "Product successfully added to your shopping cart" in modal.text
    browser.find_element(
        By.CSS_SELECTOR,
        "#blockcart-modal > div > div > div.modal-header > button > span > i",
    ).click()
    browser.find_element(
        By.CSS_SELECTOR, "#_desktop_cart > div > div > a > span.hidden-sm-down"
    ).click()
    have_product = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "#main > div > div.cart-grid-body.col-lg-8 > div > div.cart-overview.js-cart > ul > li > div > div.clearfix",
            )
        )
    )
    assert have_product.is_displayed()
