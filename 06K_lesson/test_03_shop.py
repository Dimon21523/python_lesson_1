import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _extract_amount(text: str) -> float:
    match = re.search(r"\$([0-9]+\.[0-9]{2})", text)
    if not match:
        raise AssertionError(f"Не смог найти сумму в строке: {text}")
    return float(match.group(1))


def test_shop_total():
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)

        username = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        add_buttons = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        ]
        for btn_id in add_buttons:
            wait.until(
                EC.element_to_be_clickable((By.ID, btn_id))
            ).click()

        wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Ivan")
        driver.find_element(By.ID, "last-name").send_keys("Petrov")
        driver.find_element(By.ID, "postal-code").send_keys("101000")
        driver.find_element(By.ID, "continue").click()

        total_label = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_amount = _extract_amount(total_label.text)

        assert total_amount == 58.29
    finally:
        driver.quit()
