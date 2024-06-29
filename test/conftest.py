from selenium import webdriver

import pytest


@pytest.fixture()
def browser():
    firefox_serv = webdriver.FirefoxService(executable_path="/snap/bin/geckodriver")
    firefox_web = webdriver.Firefox(service=firefox_serv)
    firefox_web.implicitly_wait(10)
    return firefox_web

