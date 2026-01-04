from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main() -> None:
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/textinput")

    wait = WebDriverWait(driver, 10)

    input_field = wait.until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("SkyPro")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    wait.until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    print(button.text)

    driver.quit()


if __name__ == "__main__":
    main()
