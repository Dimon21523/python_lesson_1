import allure
from selenium.webdriver.common.by import By
from lesson_10.pages.base_page import BasePage


class CartPage(BasePage):
    """Класс страницы корзины и товаров."""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/inventory.html"

    # Локаторы
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM_TITLE = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Добавление товара 'Backpack' в корзину")
    def add_backpack_to_cart(self) -> None:
        """Добавляет рюкзак в корзину."""
        self.driver.find_element(*self.ADD_BACKPACK).click()

    @allure.step("Переход в корзину через иконку")
    def click_cart_icon(self) -> None:
        """Кликает по иконке корзины для перехода."""
        self.driver.find_element(*self.CART_ICON).click()

    @allure.step("Получение текста названия товара в корзине")
    def get_cart_item_text(self) -> str:
        """
        Получает название товара, находящегося в корзине.
        :return: Название товара (str).
        """
        return self.driver.find_element(*self.CART_ITEM_TITLE).text
