from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_add_to_card(browser):
    main_page: MainPage = MainPage(browser).open()
    product_page: ProductPage = main_page.open_random_product()
    assert (
        "Product successfully added to your shopping cart" in product_page.add_to_cart()
    )
    product_page.close_modal()
    page_cart: CartPage = product_page.open_cart()
    product = page_cart.product_row()
    assert product.is_displayed()
