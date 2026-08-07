from pages.main_page import MainPage


def test_main_page(browser):
    page = MainPage(browser).open()
    assert page.logo().is_displayed()
    assert page.title() == "PrestaShop"
    cards = page.cards()
    assert len(cards) > 1
    page.click_like()
    expected_text = "You need to be logged in to save products in your wishlist."
    assert expected_text in page.modal_text()
    page.close_modal()
    assert len(page.cards_on_sale()) > 1
    page.click_all_new_products()
    assert "2-home" in page.current_url()
