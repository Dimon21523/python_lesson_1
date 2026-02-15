import allure
from selenium.webdriver.common.by import By
from lesson_10.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/inventory.html"

    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM_TITLE = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Добавление товара 'Backpack' в корзину")
    def add_backpack_to_cart(self) -> None:
        self.driver.find_element(*self.ADD_TO_CART_BACKPACK).click()

    @allure.step("Добавление товара 'Bolt T-Shirt' в корзину")
    def add_bolt_tshirt_to_cart(self) -> None:
        self.driver.find_element(*self.ADD_TO_CART_BOLT_TSHIRT).click()

    @allure.step("Переход в корзину через иконку")
    def click_cart_icon(self) -> None:
        self.driver.find_element(*self.CART_ICON).click()

    @allure.step("Получение текста названия товара в корзине")
    def get_cart_item_text(self) -> str:
        return self.driver.find_element(*self.CART_ITEM_TITLE).text
