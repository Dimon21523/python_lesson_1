import allure
from selenium.webdriver.common.by import By
from lesson_10.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Открытие страницы авторизации")
    def open(self) -> None:
        self.driver.get(self.url)

    @allure.step("Ввод логина: {user_name}")
    def input_user_name(self, user_name: str) -> None:
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(user_name)

    @allure.step("Ввод пароля: {password}")
    def input_password(self, password: str) -> None:
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажатие кнопки Login")
    def click_login_button(self) -> None:
        self.driver.find_element(*self.LOGIN_BUTTON).click()
