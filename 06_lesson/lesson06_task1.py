from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main() -> None:
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/ajax")

    wait = WebDriverWait(driver, 30)

    button = wait.until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )
    button.click()

    success_alert = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )

    print(success_alert.text)

    driver.quit()

if __name__ == "__main__":
    main()
