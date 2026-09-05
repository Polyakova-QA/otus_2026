import allure

from pages.clothes_pages import CLOTHES


@allure.feature("Каталог одежды")
@allure.title("Подписка на рассылку и фильтры")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression", "catalog")
def test_page_clothes(browser):
    page = CLOTHES(browser).open()
    with allure.step("Проверка: успешная подписка на рассылку"):
        assert (
            "You have successfully subscribed to this newsletter."
            in page.subscribe_newsletter()
        )
    with allure.step("Проверка: повторная подписка отклонена"):
        assert "This email address is already registered." in page.subscribe_again()
    with allure.step("Проверка: футер отображается"):
        assert page.footer().is_displayed()
    with allure.step("Проверка: заголовок подкатегорий отображается"):
        assert page.subcategories_title().is_displayed()
    with allure.step("Проверка: в блоке брендов есть нужные бренды"):
        brands = page.brands_text()
        assert "Graphic Corner" in brands and "Studio Design" in brands
    with allure.step("Проверка: активен фильтр «Black»"):
        assert "Black" in page.filter_by_black()
