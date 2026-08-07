from pages.clothes_pages import CLOTHES


def test_page_clothes(browser):
    page = CLOTHES(browser).open()
    assert (
        "You have successfully subscribed to this newsletter."
        in page.subscribe_newsletter()
    )
    assert "This email address is already registered." in page.subscribe_again()
    assert page.footer().is_displayed()
    assert page.subcategories_title().is_displayed()
    assert (
        "Graphic Corner" in page.brands_text() and "Studio Design" in page.brands_text()
    )
    assert "Black" in page.filter_by_black()
