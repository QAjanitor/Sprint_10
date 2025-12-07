import re
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидать появления элемента')
    def wait_of_element(self, locator, timeout = 3):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидать отсутствия элемента')
    def wait_of_element_invisibility(self, locator, timeout = 3):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Получить текст элемента')
    def get_text_by_locator(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Получить цифры из элемента')
    def get_numbers_by_locator(self, locator):
        text = self.driver.find_element(*locator).text
        return re.sub(r'\D', '', text)

    @allure.step('Кликнуть по элементу')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Найти элементы')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Навестись на элемент')
    def hover_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def find_element_inside(self, element, locator):
        return element.find_element(*locator)

    def find_text_inside(self, element, locator):
        return self.find_element_inside(element, locator).text