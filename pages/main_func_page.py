from selenium.webdriver import ActionChains
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

    def check_button_call_taxi_is_active(self):
        self.click_element(Locators.FAST_BUTTON)
        self.click_element(Locators.TAXI_CALL_BUTTON)
        return self.wait_of_element(Locators.TAXI_CALL_BUTTON)

    def check_change_route_type_updates_data(self):
        self.click_element(Locators.OPTIMAL_BUTTON)
        type_active_auto = self.find_element(Locators.TYPE_ACTIVE_TAB)
        optimal_text = self.get_text_by_locator(Locators.RESULT_TEXT)
        optimal_text_duration = self.get_text_by_locator(Locators.RESULT_TEXT_DURATION)
        self.click_element(Locators.FAST_BUTTON)
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
