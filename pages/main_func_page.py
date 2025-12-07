from selenium.webdriver import ActionChains
from data import TARIFFS, TARIFFS_TITLES
from locators import Locators
from pages.base_page import BasePage
import allure


class MainFuncPage(BasePage):
    order_price = 0

    @allure.step("Заполнение полей адресов: '{from_address}' -> '{to_address}'")
    def fill_addresses(self, from_address, to_address):
        with allure.step(f"Ввод адреса отправления: {from_address}"):
            from_element = self.find_element(Locators.INPUT_ADDRESS_FROM)
            action = ActionChains(self.driver)
            action.move_to_element(from_element)
            action.click()
            action.send_keys(from_address)
            action.perform()

        with allure.step(f"Ввод адреса назначения: {to_address}"):
            to_element = self.find_element(Locators.INPUT_ADDRESS_TO)
            action = ActionChains(self.driver)
            action.move_to_element(to_element)
            action.click()
            action.send_keys(to_address)
            action.perform()

    @allure.step("Заказ такси с тарифом 'Рабочий' (remember_price={remember_price})")
    def order_fast_taxi_work_tariff(self, remember_price=False):
        self.call_fast_taxi()
        self.select_tariff('Рабочий')
        if remember_price:
            self.remember_order_price()
        self.click_element(Locators.ORDER_TAXI_BUTTON)
        self.wait_of_element(Locators.POP_UP_SUCCESS_ORDER)

    @allure.step("Вызов быстрого такси через интерфейс")
    def call_fast_taxi(self):
        self.wait_of_element(Locators.FAST_BUTTON)
        self.click_element(Locators.FAST_BUTTON)
        self.wait_of_element(Locators.TAXI_CALL_BUTTON)
        self.click_element(Locators.TAXI_CALL_BUTTON)
        return self.wait_of_element(Locators.FORM_ORDER_SIX_TARIFF)

    @allure.step("Выбор тарифа: '{tariff}'")
    def select_tariff(self, tariff):
        tariffs = self.find_elements(Locators.TARIFFS)
        for tariff_card in tariffs:
            tariff_title = self.find_text_inside(tariff_card, Locators.TITLE_CURRENT_TARIFF)
            if tariff_title == tariff:
                tariff_card.click()
                allure.step(f"Выбран тариф: {tariff}")
                break

    @allure.step("Нажатие кнопки 'Отменить' в поп-апе заказа")
    def click_cancel_button(self):
        self.click_element(Locators.CANCEL_BTN)

    @allure.step("Запоминание цены заказа")
    def remember_order_price(self):
        self.order_price = self.get_numbers_by_locator(Locators.CURRENT_TARIFF_PRICE)
        allure.attach(f"Запомненная цена: {self.order_price}", name="Order Price")

    @allure.step("Проверка закрытия поп-апа заказа")
    def check_close_order_pop_up(self):
        return self.wait_of_element_invisibility(Locators.POP_UP_SUCCESS_ORDER)

    @allure.step("Сравнение цены в деталях заказа с ценой при выборе тарифа")
    def check_comparison_price_in_details_same_in_select_tariff(self):
        self.click_element(Locators.DETAILS_BTN)
        self.wait_of_element(Locators.COST_BLOCK)
        order_price_in_details = self.get_numbers_by_locator(Locators.COST_BLOCK)
        allure.attach(f"Цена в деталях: {order_price_in_details}, Запомненная цена: {self.order_price}",
                      name="Price Comparison")
        return self.order_price == order_price_in_details

    @allure.step("Проверка всех элементов в поп-апе успешного заказа")
    def check_all_elements_in_pop_up_success_order(self):
        self.wait_of_element_invisibility(Locators.SEARCH_TIMER, 60)

        elements_checked = []
        with allure.step("Проверка наличия всех элементов интерфейса"):
            min_and_arrival = self.wait_of_element(Locators.MIN_AND_ARRIVAL)
            car_number = self.wait_of_element(Locators.CAR_NUMBER)
            car_image = self.wait_of_element(Locators.CAR_IMAGE)
            avatar = self.wait_of_element(Locators.AVATAR)
            driver_name = self.wait_of_element(Locators.DRIVER_NAME)
            driver_rating = self.wait_of_element(Locators.RATING_DRIVER)

        with allure.step("Получение текстовых значений"):
            name = self.get_text_by_locator(Locators.DRIVER_NAME)
            rating = self.get_text_by_locator(Locators.RATING_DRIVER)

        result = (min_and_arrival and car_number and car_image and avatar and
                  driver_name and driver_rating and name and rating)

        allure.attach(f"Имя водителя: {name}, Рейтинг: {rating}", name="Driver Info")
        return result

    @allure.step("Выбор тарифа 'Рабочий' и опции 'ноутбук' с оформлением заказа")
    def select_work_tariff_and_laptop_with_click_order_taxi_button(self):
        self.select_tariff('Рабочий')
        self.click_element(Locators.ORDER_REQUIREMENT_BUTTON)
        self.wait_of_element(Locators.TABLE_FOR_NOTEBOOK_BUTTON)
        self.click_element(Locators.TABLE_FOR_NOTEBOOK_BUTTON)
        self.click_element(Locators.ORDER_TAXI_BUTTON)

    @allure.step("Ожидание поп-апа заказа")
    def wait_order_popup(self):
        return self.wait_of_element(Locators.POP_UP_SUCCESS_ORDER)

    @allure.step("Проверка отображения поп-апа ожидания заказа")
    def check_waiting_pop_up_waiting_order(self):
        return self.wait_order_popup()

    @allure.step("Проверка всех элементов в поп-апе ожидания заказа")
    def check_all_elements_in_pop_up_waiting_order(self):
        with allure.step("Поиск элементов интерфейса"):
            title = self.wait_of_element(Locators.SEARCHING_TITLE)
            details = self.wait_of_element(Locators.SEARCHING_TITLE)
            cancel = self.wait_of_element(Locators.SEARCHING_TITLE)
            timer = self.wait_of_element(Locators.SEARCHING_TITLE)
        return title and details and cancel and timer

    @allure.step("Проверка наличия полей и кнопки заказа такси")
    def check_existence_fields_and_button_order_taxi(self):
        phone = self.wait_of_element(Locators.PHONE)
        payment = self.wait_of_element(Locators.PAYMENT)
        comment = self.wait_of_element(Locators.COMMENT)
        requirements = self.wait_of_element(Locators.REQUIREMENTS)
        order_taxi_button = self.wait_of_element(Locators.ORDER_TAXI_BUTTON)
        result = phone and payment and comment and requirements and order_taxi_button
        allure.attach(f"Найдены все элементы: {result}", name="Form Elements Check")
        return result

    @allure.step("Проверка текстов тарифов в иконках")
    def check_texts_tariff_in_icons(self):
        tariffs = self.find_elements(Locators.TARIFFS)

        for tariff_card in tariffs:
            with allure.step("Проверка карточки тарифа"):
                tariff_card.click()
                tariff_title = self.find_text_inside(tariff_card, Locators.TITLE_CURRENT_TARIFF)

                if tariff_title not in TARIFFS_TITLES:
                    allure.step(f"Тариф '{tariff_title}' не найден в списке разрешенных")
                    return False

                info_icon = self.find_element_inside(tariff_card, Locators.ICON_CURRENT_TARIFF)
                self.hover_element(info_icon)
                self.wait_of_element(Locators.tariff_tooltip(tariff_title))

                tariff_description = self.find_text_inside(tariff_card, Locators.DESCRIPTION_CURRENT_TOOLTIP)
                expected_description = TARIFFS[tariff_title]

                if expected_description != tariff_description:
                    allure.step(f"Несоответствие описания для тарифа '{tariff_title}'")
                    allure.attach(f"Ожидалось: {expected_description}\nФактически: {tariff_description}",
                                  name="Tariff Description Mismatch")
                    return False

        allure.step("Все тарифы имеют корректные описания")
        return True

    @allure.step("Проверка отображения блока с шестью тарифами")
    def check_block_order_six_tariff(self):
        return self.call_fast_taxi()

    @allure.step("Проверка активности кнопки 'Забронировать' в кастомном маршруте")
    def check_book_a_car_button_is_active(self):
        self.click_element(Locators.CUSTOM_BUTTON)
        self.click_element(Locators.DRIVE_TYPE)
        return self.wait_of_element(Locators.BOOK_A_CAR_BUTTON)

    @allure.step("Проверка активности кнопки 'Вызвать такси' в быстром маршруте")
    def check_button_call_taxi_is_active(self):
        self.click_element(Locators.FAST_BUTTON)
        return self.wait_of_element(Locators.TAXI_CALL_BUTTON)

    @allure.step("Проверка обновления данных при переключении типа маршрута с оптимального на быстрый")
    def check_change_route_type_updates_data(self):
        with allure.step("Активация оптимального маршрута"):
            self.click_element(Locators.OPTIMAL_BUTTON)
            self.wait_of_element_invisibility(Locators.TAXI_CALL_BUTTON)
            type_active_auto = self.find_element(Locators.TYPE_ACTIVE_TAB)
            optimal_text = self.get_text_by_locator(Locators.RESULT_TEXT)
            optimal_text_duration = self.get_text_by_locator(Locators.RESULT_TEXT_DURATION)

            allure.attach(f"Оптимальный маршрут: {optimal_text}, время: {optimal_text_duration}",
                          name="Optimal Route Info")

        with allure.step("Переключение на быстрый маршрут"):
            self.click_element(Locators.FAST_BUTTON)
            self.wait_of_element(Locators.TAXI_CALL_BUTTON)
            type_active_taxi = self.find_element(Locators.TYPE_ACTIVE_TAB)
            fast_text = self.get_text_by_locator(Locators.RESULT_TEXT)
            fast_text_duration = self.get_text_by_locator(Locators.RESULT_TEXT_DURATION)

            allure.attach(f"Быстрый маршрут: {fast_text}, время: {fast_text_duration}",
                          name="Fast Route Info")

        result = (type_active_auto != type_active_taxi and
                  optimal_text != fast_text and
                  optimal_text_duration != fast_text_duration)

        allure.attach(f"Данные обновлены: {result}", name="Route Update Check")
        return result

    @allure.step("Проверка активности вкладок в кастомном типе маршрута")
    def check_activity_tab_in_custom_route_type(self):
        self.click_element(Locators.CUSTOM_BUTTON)
        types_tab = self.find_elements(Locators.TYPES)

        for type_tab in types_tab:
            classes = type_tab.get_attribute('class')
            if classes:
                class_list = classes.split()
                if 'disabled' in class_list:
                    allure.step(f"Найдена неактивная вкладка: {type_tab.text}")
                    return False

        allure.step("Все вкладки активны в кастомном маршруте")
        return True

    @allure.step("Проверка отображения точек на карте для адресов: {addresses}")
    def check_points_in_map(self, addresses):
        self.wait_of_element(Locators.POINTS)
        points = self.find_elements(Locators.POINTS)
        found_addresses = [point.text for point in points]
        found_addresses_str = ' '.join(found_addresses).lower()

        allure.attach(f"Найденные адреса: {found_addresses}", name="Found Addresses")

        for address in addresses:
            if address.lower() not in found_addresses_str:
                allure.step(f"Адрес не найден на карте: {address}")
                return False

        allure.step("Все адреса найдены на карте")
        return True

    @allure.step("Проверка отображения блока маршрута")
    def check_block_route_displayed(self):
        return self.wait_of_element(Locators.BLOCK_ROUTE)

    @allure.step("Проверка отображения текста свободного блока маршрута")
    def check_free_block_route_text_displayed(self):
        return self.wait_of_element(Locators.RESULT_TEXT_FREE_CAR_AND_0_TIME)
