import allure

from pages.administration_page import Administration
from pages.administration_products_page import AdministrationProductPage


@allure.feature("Админка: товары")
@allure.title("Создание и удаление товара")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("regression", "admin", "products")
def test_administration_product_create_and_delete(browser):
    page: Administration = Administration(browser).open()
    page.email_send("admin@example.com")
    page.password_send("Admin123!")
    page.submit()
    with allure.step("Проверка: дашборд администратора открыт"):
        assert page.dashboard_header().is_displayed()
    page_product: AdministrationProductPage = page.open_products()
    page_product.new_product()
    page_product.new_standart_product()
    page_product.hide_debug_toolbar()
    page_product.add_new_product()
    page_product.fill_product("Test Product")
    with allure.step("Проверка: товар создан"):
        assert "Successful update" in page_product.success_message()

    page_product.open_delete_modal()
    page_product.confirm_delete()
    with allure.step("Проверка: товар удалён"):
        assert "Successful deletion" in page_product.success_message()
