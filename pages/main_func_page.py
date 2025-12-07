from time import sleep

from selenium.webdriver import ActionChains

from data import TARIFFS, TARIFFS_TITLES
from locators import Locators
from pages.base_page import BasePage


class MainFuncPage(BasePage):
    def fill_addresses(self, from_address, to_address):
        from_element = self.find_element(Locators.INPUT_ADDRESS_FROM)
        action = ActionChains(self.driver)
        action.move_to_element(from_element)
        action.click()
        action.send_keys(from_address)
        action.perform()

        to_element = self.find_element(Locators.INPUT_ADDRESS_TO)
        action = ActionChains(self.driver)
        action.move_to_element(to_element)
        action.click()
        action.send_keys(to_address)
        action.perform()

    def call_fast_taxi(self):
        self.wait_of_element(Locators.FAST_BUTTON)
        self.click_element(Locators.FAST_BUTTON)
        self.wait_of_element(Locators.TAXI_CALL_BUTTON)
        self.click_element(Locators.TAXI_CALL_BUTTON)
        return self.wait_of_element(Locators.FORM_ORDER_SIX_TARIFF)

    def select_tariff(self, tariff):
        tariffs = self.find_elements(Locators.TARIFFS)
        for tariff_card in tariffs:
            tariff_title = self.find_text_inside(tariff_card, Locators.TITLE_CURRENT_TARIFF)
            if tariff_title == tariff:
                tariff_card.click()

    def select_work_tariff_and_laptop_with_click_order_taxi_button(self):
        self.select_tariff('Рабочий')
        self.click_element(Locators.ORDER_REQUIREMENT_BUTTON)
        self.wait_of_element(Locators.TABLE_FOR_NOTEBOOK_BUTTON)
        self.click_element(Locators.TABLE_FOR_NOTEBOOK_BUTTON)
        self.click_element(Locators.ORDER_TAXI_BUTTON)

    def check_waiting_pop_up_success_order(self):
        return self.wait_of_element(Locators.POP_UP_SUCCESS_ORDER)

    def check_all_elements_in_pop_up_success_order(self):
        title = self.wait_of_element(Locators.SEARCHING_TITLE)
        details = self.wait_of_element(Locators.SEARCHING_TITLE)
        cancel = self.wait_of_element(Locators.SEARCHING_TITLE)
        timer = self.wait_of_element(Locators.SEARCHING_TITLE)
        return title and details and cancel and timer

    def check_existence_fields_and_button_order_taxi(self):
        phone = self.wait_of_element(Locators.PHONE)
        payment = self.wait_of_element(Locators.PAYMENT)
        comment = self.wait_of_element(Locators.COMMENT)
        requirements = self.wait_of_element(Locators.REQUIREMENTS)
        order_taxi_button = self.wait_of_element(Locators.ORDER_TAXI_BUTTON)
        result = phone and payment and comment and requirements and order_taxi_button
        return result

    def check_texts_tariff_in_icons(self):
        tariffs = self.find_elements(Locators.TARIFFS)
        for tariff_card in tariffs:
            tariff_card.click()

            tariff_title = self.find_text_inside(tariff_card, Locators.TITLE_CURRENT_TARIFF)
            if tariff_title not in TARIFFS_TITLES:
                return False

            info_icon = self.find_element_inside(tariff_card, Locators.ICON_CURRENT_TARIFF)
            self.hover_element(info_icon)
            self.wait_of_element(Locators.tariff_tooltip(tariff_title))

            tariff_description = self.find_text_inside(tariff_card, Locators.DESCRIPTION_CURRENT_TOOLTIP)
            expected_description = TARIFFS[tariff_title]
            if expected_description != tariff_description:
                return False

        return True

    def check_block_order_six_tariff(self):
        return self.call_fast_taxi()

    def check_book_a_car_button_is_active(self):
        self.click_element(Locators.CUSTOM_BUTTON)
        self.click_element(Locators.DRIVE_TYPE)
        return self.wait_of_element(Locators.BOOK_A_CAR_BUTTON)

    def check_button_call_taxi_is_active(self):
        self.click_element(Locators.FAST_BUTTON)
        return self.wait_of_element(Locators.TAXI_CALL_BUTTON)

    def check_change_route_type_updates_data(self):
        self.click_element(Locators.OPTIMAL_BUTTON)
        self.wait_of_element_invisibility(Locators.TAXI_CALL_BUTTON)
        type_active_auto = self.find_element(Locators.TYPE_ACTIVE_TAB)
        optimal_text = self.get_text_by_locator(Locators.RESULT_TEXT)
        optimal_text_duration = self.get_text_by_locator(Locators.RESULT_TEXT_DURATION)
        self.click_element(Locators.FAST_BUTTON)
        self.wait_of_element(Locators.TAXI_CALL_BUTTON)
        type_active_taxi = self.find_element(Locators.TYPE_ACTIVE_TAB)
        fast_text = self.get_text_by_locator(Locators.RESULT_TEXT)
        fast_text_duration = self.get_text_by_locator(Locators.RESULT_TEXT_DURATION)
        return type_active_auto != type_active_taxi and optimal_text != fast_text and optimal_text_duration != fast_text_duration

    def check_activity_tab_in_custom_route_type(self):
        self.click_element(Locators.CUSTOM_BUTTON)
        types_tab = self.find_elements(Locators.TYPES)
        for type_tab in types_tab:
            classes = type_tab.get_attribute('class')
            if classes:
                class_list = classes.split()
                if 'disabled' in class_list:
                    return False
        return True

    def check_points_in_map(self, addresses):
        self.wait_of_element(Locators.POINTS)
        points = self.find_elements(Locators.POINTS)
        found_addresses = [point.text for point in points]
        found_addresses_str = ' '.join(found_addresses).lower()
        for address in addresses:
            if address.lower() not in found_addresses_str:
                return False
        return True

    def check_block_route_displayed(self):
        return self.wait_of_element(Locators.BLOCK_ROUTE)

    def check_free_block_route_text_displayed(self):
        return self.wait_of_element(Locators.RESULT_TEXT_FREE_CAR_AND_0_TIME)
