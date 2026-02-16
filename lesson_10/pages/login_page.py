import allure
from selenium.webdriver.common.by import By
from lesson_10.pages.base_page import BasePage


class LoginPage(BasePage):
    """Класс страницы авторизации."""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    # Локаторы
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Открытие страницы авторизации")
    def open(self) -> None:
        """Открывает страницу авторизации."""
        self.driver.get(self.url)

    @allure.step("Ввод логина: {user_name}")
    def input_user_name(self, user_name: str) -> None:
        """
        Вводит имя пользователя в поле логина.
        :param user_name: Имя пользователя (str).
        """
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(user_name)

    @allure.step("Ввод пароля")
    def input_password(self, password: str) -> None:
        """
        Вводит пароль в поле пароля.
        :param password: Пароль (str).
        """
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажатие кнопки Login")
    def click_login_button(self) -> None:
        """Нажимает кнопку входа."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
