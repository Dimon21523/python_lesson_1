from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def main() -> None:
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    wait = WebDriverWait(driver, 15)

    def third_image_src(driver_instance):
        images = driver_instance.find_elements(By.CSS_SELECTOR, "img")
        if len(images) < 3:
            return False
        src = images[2].get_attribute("src")
        return src if src else False

    third_src = wait.until(third_image_src)

    print(third_src)

    driver.quit()


if __name__ == "__main__":
    main()
