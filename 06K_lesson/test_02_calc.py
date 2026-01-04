from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = (
    "https://bonigarcia.dev/selenium-webdriver-java/"
    "slow-calculator.html"
)


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 10)

        delay = wait.until(
            EC.visibility_of_element_located((By.ID, "delay"))
        )
        delay.clear()
        delay.send_keys("45")

        def click_btn(text: str):
            btn = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//span[text()='{text}']")
                )
            )
            btn.click()

        click_btn("7")
        click_btn("+")
        click_btn("8")
        click_btn("=")

        screen = driver.find_element(By.CSS_SELECTOR, ".screen")
        result_wait = WebDriverWait(driver, 50)
        result_wait.until(lambda d: screen.text.strip() == "15")

        assert screen.text.strip() == "15"
    finally:
        driver.quit()
