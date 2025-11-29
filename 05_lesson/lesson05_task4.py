from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def main() -> None:
    options = Options()
    driver = webdriver.Firefox(options=options)

    driver.get(" http://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.TAG_NAME, "button")
    login_button.click()

    success_message = driver.find_element(By.ID, "flash").text
    print("\nSUCCESS MESSAGE:")
    print(success_message)

    driver.quit()

if __name__ == "__main__":
    main()
