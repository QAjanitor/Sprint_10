import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидать появления элемента')
    def wait_of_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    # @allure.step('Получить текст элемента')
    # def get_text_by_locator(self, locator):
    #     return self.driver.find_element(*locator).text

    # @allure.step('Кликнуть по элементу с индексом {index}')
    # def click_by_index(self, locator, index):
    #     self.driver.find_elements(*locator)[index].click()

    # @allure.step('Кликнуть по элементу')
    # def click_element(self, locator):
    #     self.driver.find_element(*locator).click()

    # @allure.step('Ввести текст: {value}')
    # def send_keys(self, locator, value):
    #     self.driver.find_element(*locator).send_keys(value)

    @allure.step('Найти элементы')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)
