import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    return browser


@pytest.fixture()
def url():
    url = "http://localhost:3000/"
    return url