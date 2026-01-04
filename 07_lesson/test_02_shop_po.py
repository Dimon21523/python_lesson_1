from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_page_object():
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.add_tshirt()
        inventory.add_onesie()
        inventory.open_cart()

        cart = CartPage(driver)
        cart.checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_form("Ivan", "Petrov", "101000")

        assert checkout.get_total() == 58.29
    finally:
        driver.quit()
