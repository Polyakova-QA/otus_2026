from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


def test_card_product(browser, base_url):
    browser.get(base_url + "women/2-9-brown-bear-printed-sweater.html#/1-size-s")
    wait = WebDriverWait(browser, 2)
    have_description = browser.find_element(By.CSS_SELECTOR, "#description > div > p")
    assert have_description.is_displayed()
    assert (
        "Studio Design' PolyFaune collection features classic products with colorful patterns"
        in have_description.text
    )
    browser.find_element(
        By.CSS_SELECTOR,
        "#main > div.row.product-container.js-product-container > div:nth-child(2) > div.product-information > div.tabs > ul > li:nth-child(2) > a",
    ).click()
    modal_data_sheet = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#product-details > section > dl")
        )
    )
    assert "Composition" in modal_data_sheet.text
    assert "Long Sleeves" in modal_data_sheet.text
    assert "Farry" not in modal_data_sheet.text
    browser.find_element(
        By.CSS_SELECTOR,
        "#content > div.images-container.js-images-container > div.product-cover > div",
    ).click()
    modal = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "#product-modal > div > div > div > figure > picture > img",
            )
        )
    )
    assert modal.is_displayed()
    assert modal.get_attribute("src")
    assert ".jpg" in modal.get_attribute("src")
    size = modal.size
    assert size["width"] >= 800
