from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main() -> None:
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/classattr")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
    )
    button.click()

    driver.quit()

if __name__ == "__main__":
    main()
