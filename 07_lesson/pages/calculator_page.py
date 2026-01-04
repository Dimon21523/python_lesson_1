from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value):
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(value)

    def click_button(self, text):
        button = self.driver.find_element(
            By.XPATH,
            f"//span[text()='{text}']"
        )
        button.click()

    def get_result(self):
        screen = self.driver.find_element(By.CLASS_NAME, "screen")
        self.wait.until(lambda d: screen.text.strip() == "15")
        return screen.text.strip()
