import allure

from pages.main_page import MainPage


@allure.feature("Главная страница")
@allure.title("Проверка элементов главной страницы")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("smoke", "main-page")
def test_main_page(browser):
    page = MainPage(browser).open()
    with allure.step("Проверка: логотип отображается"):
        assert page.logo().is_displayed()
    with allure.step("Проверка: заголовок вкладки «PrestaShop»"):
        assert page.title() == "PrestaShop"
    cards = page.cards()
    with allure.step("Проверка: на странице больше одной карточки"):
        assert len(cards) > 1
    page.click_like()
    expected_text = "You need to be logged in to save products in your wishlist."
    with allure.step("Проверка: текст модального окна wishlist"):
        assert expected_text in page.modal_text()
    page.close_modal()
    with allure.step("Проверка: есть товары со скидкой"):
        assert len(page.cards_on_sale()) > 1
    page.click_all_new_products()
    with allure.step("Проверка: переход на страницу всех товаров"):
        assert "2-home" in page.current_url()
