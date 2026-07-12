

def test_title(browser):
    browser.get('http://localhost:8081/')
    assert "PrestaShop" in browser.title