from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import pytest
from time import sleep


@pytest.fixture()
def driver():
    geckodriver_path = "/snap/bin/geckodriver"
    fire_service = webdriver.FirefoxService(executable_path=geckodriver_path)
    firefox_driver = webdriver.Firefox(service=fire_service)
    return firefox_driver


def test_insider(driver):
    try:
        driver.get(
            "https://oroinc.com/b2b-ecommerce/integrations/?utm_source=google&utm_medium=cpc&utm_campaign=Non-Brand%20%7C%20EU%20%7C%20Search&utm_content=B2B%20Ecomm&utm_term=manufacturing%20ecommerce%20software&matchtype=p&gad_source=1&gclid=CjwKCAjw-O6zBhASEiwAOHeGxcUcwR-0UMwPt_jl9TBlcdpM3figaT8Dp67qv4mWUhTOik7WBxu2TxoCYtQQAvD_BwE")

        link_about = driver.find_element(By.XPATH, "//a[text()='About']")
        link_company = driver.find_element(By.XPATH, "//a[text()='Company' and @role='menuitem']")
        ActionChains(driver).click(link_about).click(link_company).perform()

    finally:
        sleep(2)
        driver.close()

