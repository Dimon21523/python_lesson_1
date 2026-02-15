import allure
from lesson_10.pages.login_page import LoginPage
from lesson_10.pages.cart_page import CartPage


@allure.epic("Веб-интерфейс")
@allure.feature("Корзина")
@allure.story("Добавление товаров")
class TestCart:

    @allure.title("Добавление товара в корзину")
    @allure.description("Проверка, что товар отображается в корзине")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_cart(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.input_user_name("standard_user")
        login_page.input_password("secret_sauce")
        login_page.click_login_button()

        cart_page = CartPage(driver)
        cart_page.add_backpack_to_cart()
        cart_page.click_cart_icon()

        with allure.step("Проверка товара в корзине"):
            assert "Sauce Labs Backpack" == cart_page.get_cart_item_text()
