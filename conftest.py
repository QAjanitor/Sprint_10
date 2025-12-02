from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
import pytest
import os

from pages.main_func_page import MainFuncPage
from urls import BASE_URL


@pytest.fixture
def main_func_page(driver):
    return MainFuncPage(driver)

# @pytest.fixture
# def random_user_payload_for_create():
#     fake = Faker('ru_RU')
#     return {
#         'first_name': fake.first_name(),
#         'last_name': fake.last_name(),
#         'user_name': fake.user_name(),
#         'email': fake.email(),
#         'password': fake.password()
#     }


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



# @pytest.fixture
# def receipt_payload():
#     fake = Faker('ru_RU')
#     food = Food(locale=Locale.RU)
#     return {
#         'name': food.dish(),
#         'ingredient_amount': fake.random_int(min=5, max=500),
#         'cooking_time': fake.random_int(min=10, max=120),
#         'description': fake.text(max_nb_chars=200)
#     }