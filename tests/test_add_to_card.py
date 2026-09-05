import allure

from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@allure.feature("Корзина")
@allure.title("Добавление случайного товара в корзину")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "cart", "positive")
def test_add_to_card(browser):
    main_page: MainPage = MainPage(browser).open()
    product_page: ProductPage = main_page.open_random_product()
    with allure.step("Проверка: товар добавлен в корзину"):
        assert "ерунда" in product_page.add_to_cart()
    product_page.close_modal()
    page_cart: CartPage = product_page.open_cart()
    product = page_cart.product_row()
    with allure.step("Проверка: товар отображается в корзине"):
        assert product.is_displayed()
