from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

    def add_tshirt(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

    def add_onesie(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

    def open_cart(self):
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
