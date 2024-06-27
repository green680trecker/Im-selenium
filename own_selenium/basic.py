from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
#ActionChains

geckodriver_path = "/snap/bin/geckodriver"
fire_service = webdriver.FirefoxService(executable_path=geckodriver_path)

browser = webdriver.Firefox(service=fire_service)
url = "https://www.qa-practice.com/elements/button/simple"
browser.get(url)

#CSS_SELECTOR . # * ^ $ | ~ > +
# browser.find_element(By.CSS_SELECTOR, "input[type=submit].btn").click()
# browser.find_element(By.CSS_SELECTOR, 'input[id="submit-id-submit"]').click()

#XPATH tag or * and so on[@(attribute)="???"][index] contains child following text() descendant following-sibling preceding
# browser.find_element(By.XPATH, "//input[@id='submit-id-submit']").click()
browser.get("https://www.qa-practice.com/elements/textarea/single")
browser.find_element(By.XPATH, "//form[@method='post']/child::input[2]").click()



sleep(2)
browser.close()

#allure report, Gitlab CI/CD
#end-to-end
