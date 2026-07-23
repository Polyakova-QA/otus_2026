from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize("currency", [""], indirect=True)
def test_currency_main(browser, base_url, currency):
    assert currency["usd"] != currency["euro"]
