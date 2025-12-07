from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
import pytest

from data import ADDRESSES
from pages.main_func_page import MainFuncPage
from urls import BASE_URL


@pytest.fixture
def main_func_page(driver):
    return MainFuncPage(driver)

@pytest.fixture
def main_func_page_filled_addresses(main_func_page):
    main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
    return main_func_page

@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()
