import allure

from pages.card_product_page import CardPage


@allure.feature("Карточка товара")
@allure.title("Проверка карточки товара")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression", "product-card")
def test_card_product(browser):
    page = CardPage(browser).open()
    with allure.step("Проверка: описание товара содержит нужный текст"):
        assert (
            "Studio Design' PolyFaune collection features classic products "
            "with colorful patterns" in page.have_description()
        )
    details = page.product_details()
    with allure.step("Проверка: характеристики содержат нужные значения"):
        assert "Composition" in details
        assert "Long Sleeves" in details
        assert "Cotton" in details
    modal = page.click_picture()
    with allure.step("Проверка: изображение открылось и корректно"):
        assert modal.get_attribute("src")
        assert ".jpg" in modal.get_attribute("src")
        assert modal.size["width"] >= 800
