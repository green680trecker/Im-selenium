from selenium.webdriver.common.by import By


def test_simple_button1_show(browser):
    browser.get("https://www.qa-practice.com/elements/button/simple")
    browser.find_element(By.ID, "submit-id-submit").is_displayed()
    browser.close()


def test_simple_button2_click(browser):
    browser.get("https://www.qa-practice.com/elements/button/simple")
    browser.find_element(By.ID, "submit-id-submit").click()
    browser.close()
