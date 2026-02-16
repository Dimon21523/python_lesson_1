import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для страниц веб-приложения."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Открытие страницы по URL: {url}")
    def get_url(self, url: str) -> None:
        """
        Открывает страницу по указанному URL.
        :param url: Ссылка на страницу (str).
        """
        self.driver.get(url)

    @allure.step("Поиск элемента по локатору: {locator}")
    def find_element(self, locator: tuple, time: int = 10) -> WebElement:
        """
        Ищет один элемент на странице с ожиданием.
        :param locator: Локатор элемента (tuple).
        :param time: Время ожидания в секундах (int).
        :return: Найденный веб-элемент (WebElement).
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    @allure.step("Поиск списка элементов по локатору: {locator}")
    def find_elements(self, locator: tuple, t: int = 10) -> list[WebElement]:
        """
        Ищет список элементов на странице с ожиданием.
        :param locator: Локатор элементов (tuple).
        :param t: Время ожидания в секундах (int).
        :return: Список найденных веб-элементов (list[WebElement]).
        """
        return WebDriverWait(self.driver, t).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    @allure.step("Получение текущего URL")
    def get_current_url(self) -> str:
        """
        Возвращает текущий URL страницы.
        :return: URL страницы (str).
        """
        return self.driver.current_url
