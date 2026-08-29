from selenium.webdriver.common.by import By


# ─────────────────────────── Общие компоненты шапки ───────────────────────────
class HeaderLocators:
    LOGO = (By.CSS_SELECTOR, "#_desktop_logo img")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "#_desktop_user_info > div > a.account > span")
    LOGOUT = (By.CSS_SELECTOR, "#_desktop_user_info a[href*='mylogout']")
    SIGN_IN = (By.CSS_SELECTOR, "#_desktop_user_info > div > a > span")
    CART_LINK = (
        By.CSS_SELECTOR,
        "#_desktop_cart > div > div > a > span.hidden-sm-down",
    )


# ─────────────────────────── Компонент выбора валюты ───────────────────────────
class CurrencySelectorLocators:
    PRICE = (By.CSS_SELECTOR, ".product-price-and-shipping .price")
    TOGGLE = (By.CSS_SELECTOR, "#_desktop_currency_selector > div > button")
    USD_OPTION = (
        By.CSS_SELECTOR,
        "#_desktop_currency_selector > div > ul > li:nth-child(2) > a",
    )


# ─────────────────────────────── login ───────────────────────────────
# test_authorization.py
class LoginLocators:
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, "#submit-login")
    # ACCOUNT_NAME / LOGOUT / SIGN_IN → см. HeaderLocators


# ─────────────────────────────── registration ───────────────────────────────
# test_registration.py
class RegistrationLocators:
    TITLE = (By.CSS_SELECTOR, "#main > header > h1")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SHOW_PASSWORD_BTN = (
        By.CSS_SELECTOR,
        "#customer-form > div > div.field-password-policy > div > "
        "div.col-md-6.js-input-column > div.input-group.js-parent-focus > span > button",
    )
    PASSWORD_LENGTH_HINT = (
        By.CSS_SELECTOR,
        "#customer-form > div > div.field-password-policy > div > "
        "div.col-md-6.js-input-column > div:nth-child(2) > div > "
        "div.password-requirements > p.password-requirements-length",
    )
    PASSWORD_SCORE_HINT = (
        By.CSS_SELECTOR,
        "#customer-form > div > div.field-password-policy > div > "
        "div.col-md-6.js-input-column > div:nth-child(2) > div > "
        "div.password-requirements > p.password-requirements-score > span",
    )
    SUBMIT = (By.CSS_SELECTOR, "#customer-form > footer > button")
    FIRSTNAME = (By.CSS_SELECTOR, "#field-firstname")
    LASTNAME = (By.CSS_SELECTOR, "#field-lastname")
    CHECK_AGREE = (By.CSS_SELECTOR, "#customer-form input[name='psgdpr']")
    CHECK_PRIVACY = (By.CSS_SELECTOR, "#customer-form input[name='customer_privacy']")
    EMAIL = (By.CSS_SELECTOR, "#field-email")


# ─────────────────────────────── administration ───────────────────────────────
# test_administration.py
class AdministrationLocators:
    EMAIL_LABEL = (By.CSS_SELECTOR, "#login_form > div:nth-child(2) > label")
    PASSWORD_LABEL = (By.CSS_SELECTOR, "#login_form > div:nth-child(3) > label")
    SUBMIT = (By.CSS_SELECTOR, "#submit_login")
    EMAIL_ERROR = (By.CSS_SELECTOR, "#login_form > div:nth-child(2) > span")
    STAY_LOGGED_IN = (By.CSS_SELECTOR, "#stay_logged_in")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "#forgot-password-link")
    RESET_PASSWORD_BTN = (By.CSS_SELECTOR, "#reset-password-button")
    EMAIL_FORGOT = (By.CSS_SELECTOR, "#email_forgot")
    RESET_ERROR = (By.CSS_SELECTOR, "#error > p")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#passwd")
    DASHBOARD_HEADER = (By.CSS_SELECTOR, "#content > div.bootstrap > div > div > h1")
    CATALOG = (By.CSS_SELECTOR, "#subtab-AdminCatalog > a > span")
    PRODUCTS = (By.CSS_SELECTOR, "#subtab-AdminProducts > a")
    OPEN_DASHBOARD = (By.CSS_SELECTOR, "#tab-AdminDashboard > a > span")


# ─────────────────────────────── administration_product ───────────────────────────────
# test_administration_products_page.py
class AdministrationPageLocatorsProducts:
    NEW_PRODUCT = (By.CSS_SELECTOR, "#page-header-desc-configuration-add")
    STANDART_PRODUCT = (
        By.CSS_SELECTOR,
        "button.product-type-choice[data-value='standard']",
    )
    ADD_PRODUCT = (By.CSS_SELECTOR, "#create_product_create")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#product_header_name_1")
    SAVE = (By.CSS_SELECTOR, "#product_footer_save")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alert-text p")
    DELETE_DROPDOWN = (By.CSS_SELECTOR, "#product_footer_actions_dropdown")
    DELETE_PRODUCT = (By.CSS_SELECTOR, "#product_footer_actions_delete")
    CONFIRM_DELETE = (
        By.CSS_SELECTOR,
        "#delete-product-footer-modal .btn-confirm-submit",
    )


# ─────────────────────── Главная страница (base_url) ───────────────────────
# test_my_store_main_page.py  +  test_add_to_card.py (выбор товара)
class MainPageLocators:
    PRODUCT_MINIATURES = (By.CSS_SELECTOR, "#content article.product-miniature")
    FIRST_PRODUCT_LIKE = (
        By.CSS_SELECTOR,
        "#content > section:nth-child(2) > div > div:nth-child(1) > article > "
        "div > button > i",
    )
    MODAL_TEXT = (
        By.CSS_SELECTOR,
        "#footer > div.footer-container > div > div:nth-child(1) > div.wishlist-login > "
        "div.wishlist-modal.modal.fade.show > div > div > div.modal-body > p",
    )
    MODAL_CLOSE = (
        By.CSS_SELECTOR,
        "#footer > div.footer-container > div > div:nth-child(1) > div.wishlist-login > "
        "div.wishlist-modal.modal.fade.show > div > div > div.modal-header > button",
    )
    PRODUCTS_ON_SALE = (
        By.CSS_SELECTOR,
        "#content section:nth-child(5) article.product-miniature",
    )
    ALL_NEW_PRODUCTS_LINK = (By.PARTIAL_LINK_TEXT, "All products")


# ─────────────────────────────── Карточка товара ───────────────────────────────
# test_card_product.py  +  test_add_to_card.py (добавление в корзину)
class ProductPageLocators:
    ADD_TO_CART = (
        By.CSS_SELECTOR,
        "#add-to-cart-or-refresh > div.product-add-to-cart.js-product-add-to-cart > "
        "div > div.add > button",
    )
    ADDED_MODAL_LABEL = (By.CSS_SELECTOR, "#myModalLabel")
    ADDED_MODAL_CLOSE = (
        By.CSS_SELECTOR,
        "#blockcart-modal > div > div > div.modal-header > button > span > i",
    )
    DESCRIPTION = (By.CSS_SELECTOR, "#description > div > p")
    PRODUCT_DETAILS = (
        By.CSS_SELECTOR,
        "#main > div.row.product-container.js-product-container > div:nth-child(2) > "
        "div.product-information > div.tabs > ul > li:nth-child(2) > a",
    )
    DATA_SHEET = (By.CSS_SELECTOR, "#product-details > section > dl")
    PRODUCT_PICTURE = (
        By.CSS_SELECTOR,
        "#content > div.images-container.js-images-container > div.product-cover > div",
    )
    PRODUCT_MODAL_IMG = (
        By.CSS_SELECTOR,
        "#product-modal > div > div > div > figure > picture > img",
    )


# ─────────────────────────────── Корзина ───────────────────────────────
# test_add_to_card.py
class CartPageLocators:
    PRODUCT_ROW = (
        By.CSS_SELECTOR,
        "#main > div > div.cart-grid-body.col-lg-8 > div > div.cart-overview.js-cart > "
        "ul > li > div > div.clearfix",
    )


# ─────────────────── Категория "Clothes" (3-clothes) ───────────────────
# test_page_clothes.py
class ClothesCategoryLocators:
    NEWSLETTER_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    NEWSLETTER_SUBMIT = (By.CSS_SELECTOR, "input[name='submitNewsletter']")
    NEWSLETTER_MODAL = (
        By.CSS_SELECTOR,
        "#blockEmailSubscription_displayFooterBefore > div > div > form > p",
    )
    FOOTER = (By.CSS_SELECTOR, "#footer > div.footer-container")
    SUBCATEGORIES_TITLE = (By.CSS_SELECTOR, "#subcategories > h2")
    BRANDS_SECTION = (By.CSS_SELECTOR, "#search_filters_brands > section")
    FILTER_BLACK = (
        By.XPATH,
        "//*[@id='search_filters']//a[contains(normalize-space(.), 'Black')]",
    )
    ACTIVE_FILTER = (By.CSS_SELECTOR, "#js-active-search-filters > ul > li")
