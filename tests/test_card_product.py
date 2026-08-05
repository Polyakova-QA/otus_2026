from pages.card_product_page import CardPage


def test_card_product(browser, base_url):
    page = CardPage(browser, base_url).open()
    assert (
        "Studio Design' PolyFaune collection features classic products with colorful patterns"
        in page.have_description()
    )
    assert "Composition" in page.product_details()
    assert "Long Sleeves" in page.product_details()
    assert "Cotton" in page.product_details()
    modal = page.click_picture()
    assert modal.get_attribute("src")
    assert ".jpg" in modal.get_attribute("src")
    size = modal.size
    assert size["width"] >= 800
