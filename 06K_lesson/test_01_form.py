from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"


def _classes(el):
    return (el.get_attribute("class") or "").lower()


def _is_red(el):
    c = _classes(el)
    return "alert-danger" in c or "is-invalid" in c


def _is_green(el):
    c = _classes(el)
    return "alert-success" in c or "is-valid" in c


def _find_one(driver, wait, locators, field_name):
    for by, value in locators:
        try:
            el = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((by, value))
            )
            return el
        except Exception:
            continue
    raise AssertionError(f"Не найдено поле: {field_name}")


def test_form():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 20)

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        fields = [
            (
                "first_name",
                [
                    (By.ID, "first-name"),
                    (By.NAME, "first-name"),
                    (By.XPATH, "//input[@placeholder='First name']"),
                ],
                "Иван",
            ),
            (
                "last_name",
                [
                    (By.ID, "last-name"),
                    (By.NAME, "last-name"),
                    (By.XPATH, "//input[@placeholder='Last name']"),
                ],
                "Петров",
            ),
            (
                "address",
                [
                    (By.ID, "address"),
                    (By.NAME, "address"),
                    (By.XPATH, "//input[@placeholder='Address']"),
                ],
                "Ленина, 55-3",
            ),
            (
                "email",
                [
                    (By.ID, "email"),
                    (By.ID, "e-mail"),
                    (By.NAME, "email"),
                    (By.NAME, "e-mail"),
                    (By.XPATH, "//input[@placeholder='Email']"),
                ],
                "test@skypro.com",
            ),
            (
                "phone",
                [
                    (By.ID, "phone-number"),
                    (By.ID, "phone"),
                    (By.NAME, "phone-number"),
                    (By.NAME, "phone"),
                    (By.XPATH, "//input[@placeholder='Phone number']"),
                ],
                "+7985899998787",
            ),
            (
                "city",
                [
                    (By.ID, "city"),
                    (By.NAME, "city"),
                    (By.XPATH, "//input[@placeholder='City']"),
                ],
                "Москва",
            ),
            (
                "country",
                [
                    (By.ID, "country"),
                    (By.NAME, "country"),
                    (By.XPATH, "//input[@placeholder='Country']"),
                ],
                "Россия",
            ),
            (
                "job_position",
                [
                    (By.ID, "job-position"),
                    (By.NAME, "job-position"),
                    (By.XPATH, "//input[@placeholder='Job position']"),
                ],
                "QA",
            ),
            (
                "company",
                [
                    (By.ID, "company"),
                    (By.NAME, "company"),
                    (By.XPATH, "//input[@placeholder='Company']"),
                ],
                "SkyPro",
            ),
        ]

        for field_name, locators, value in fields:
            el = _find_one(driver, wait, locators, field_name)
            el.clear()
            el.send_keys(value)

        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit.click()

        zip_input = _find_one(
            driver,
            wait,
            [
                (By.ID, "zip-code"),
                (By.NAME, "zip-code"),
                (By.XPATH, "//input[@placeholder='Zip code']"),
            ],
            "zip_code",
        )
        zip_parent = zip_input.find_element(By.XPATH, "./..")

        wait.until(lambda d: _is_red(zip_input) or _is_red(zip_parent))
        assert _is_red(zip_input) or _is_red(zip_parent)

        for field_name, locators, _value in fields:
            inp = _find_one(driver, wait, locators, field_name)
            parent = inp.find_element(By.XPATH, "./..")
            assert _is_green(inp) or _is_green(parent)

    finally:
        driver.quit()
