import allure
from lesson_10.pages.login_page import LoginPage


@allure.epic("Веб-интерфейс")
@allure.feature("Авторизация")
@allure.story("Вход в систему")
class TestLogin:

    @allure.title("Успешная авторизация")
    @allure.description("Проверка входа с валидными данными")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_success(self, driver):
        page = LoginPage(driver)
        page.open()

        page.input_user_name("standard_user")
        page.input_password("secret_sauce")
        page.click_login_button()

        with allure.step("Проверка перехода на inventory.html"):
            assert "inventory" in page.get_current_url()

    @allure.title("Авторизация с некорректными данными")
    @allure.description("Проверка ошибки при вводе неверного пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_failure(self, driver):
        page = LoginPage(driver)
        page.open()

        page.input_user_name("standard_user")
        page.input_password("wrong_password")
        page.click_login_button()

        with allure.step("Проверка, что URL не изменился"):
            assert page.get_current_url() == "https://www.saucedemo.com/"
