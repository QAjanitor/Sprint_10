import re
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание появления элемента: {locator}')
    def wait_of_element(self, locator, timeout=3):
        with allure.step(f"Установка таймаута ожидания: {timeout} секунд"):
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            allure.attach(
                f"Элемент найден: {locator}",
                name="Element Found",
                attachment_type=allure.attachment_type.TEXT
            )
            return element

    @allure.step('Ожидание исчезновения элемента: {locator}')
    def wait_of_element_invisibility(self, locator, timeout=3):
        with allure.step(f"Проверка исчезновения элемента в течение {timeout} секунд"):
            result = WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            allure.attach(
                f"Элемент скрыт: {locator}",
                name="Element Hidden",
                attachment_type=allure.attachment_type.TEXT
            )
            return result

    @allure.step('Получение текста элемента: {locator}')
    def get_text_by_locator(self, locator):
        with allure.step("Поиск элемента на странице"):
            element = self.driver.find_element(*locator)
            text = element.text
            allure.attach(
                f"Получен текст: '{text}'",
                name="Text Content",
                attachment_type=allure.attachment_type.TEXT
            )
            return text

    @allure.step('Извлечение чисел из текста элемента: {locator}')
    def get_numbers_by_locator(self, locator):
        with allure.step("Получение текста из элемента"):
            text = self.driver.find_element(*locator).text

        with allure.step("Извлечение числовых значений"):
            numbers = re.sub(r'\D', '', text)

        allure.attach(
            f"Исходный текст: '{text}' → Извлеченные числа: '{numbers}'",
            name="Number Extraction",
            attachment_type=allure.attachment_type.TEXT
        )
        return numbers

    @allure.step('Клик по элементу: {locator}')
    def click_element(self, locator):
        with allure.step("Поиск элемента для клика"):
            element = self.driver.find_element(*locator)

        with allure.step("Выполнение клика"):
            element.click()

        allure.attach(
            f"Клик выполнен по элементу: {locator}",
            name="Element Clicked",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step('Поиск всех элементов по локатору: {locator}')
    def find_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        allure.attach(
            f"Найдено элементов: {len(elements)}",
            name="Elements Count",
            attachment_type=allure.attachment_type.TEXT
        )
        return elements

    @allure.step('Поиск элемента по локатору: {locator}')
    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        allure.attach(
            f"Элемент найден: {locator}",
            name="Element Found",
            attachment_type=allure.attachment_type.TEXT
        )
        return element

    @allure.step('Наведение курсора на элемент')
    def hover_element(self, element):
        with allure.step("Создание цепочки действий"):
            action = ActionChains(self.driver)

        with allure.step("Добавление действия наведения"):
            action.move_to_element(element)

        with allure.step("Выполнение действия"):
            action.perform()

        allure.attach(
            "Наведение на элемент выполнено",
            name="Hover Performed",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step('Поиск элемента внутри родительского элемента')
    def find_element_inside(self, element, locator):
        inner_element = element.find_element(*locator)
        allure.attach(
            f"Вложенный элемент найден внутри родительского",
            name="Inner Element Found",
            attachment_type=allure.attachment_type.TEXT
        )
        return inner_element

    @allure.step('Получение текста внутри элемента')
    def find_text_inside(self, element, locator):
        with allure.step("Поиск вложенного элемента"):
            inner_element = self.find_element_inside(element, locator)

        with allure.step("Извлечение текста"):
            text = inner_element.text

        allure.attach(
            f"Текст внутри элемента: '{text}'",
            name="Inner Text",
            attachment_type=allure.attachment_type.TEXT
        )
        return text
