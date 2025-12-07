import pytest
from data import ADDRESSES


class TestE2ETaxiOrder:
    def test_select_work_tariff_with_laptop_table_option(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        main_func_page.call_fast_taxi()
        main_func_page.select_work_tariff_and_laptop_with_click_order_taxi_button()
        assert main_func_page.check_waiting_pop_up_waiting_order()
        assert main_func_page.check_all_elements_in_pop_up_waiting_order()

    def test_wait_for_driver_search_timer(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        main_func_page.call_fast_taxi()
        main_func_page.select_work_tariff_and_laptop_with_click_order_taxi_button()
        main_func_page.wait_order_popup()
        assert main_func_page.check_all_elements_in_pop_up_success_order()

    def test_price_in_details_same_in_select_tariff(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        main_func_page.call_fast_taxi()
        main_func_page.select_work_tariff_and_laptop_with_click_order_taxi_button()
        main_func_page.remember_order_price()
        main_func_page.wait_order_popup()
        assert main_func_page.check_comparison_price_in_details_same_in_select_tariff()

    @pytest.mark.xfail(reason="Не работает кнопка 'Отменить' на поп-апе заказа такси")
    def test_click_button_cancel_in_pop_up_order(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        main_func_page.call_fast_taxi()
        main_func_page.select_work_tariff_and_laptop_with_click_order_taxi_button()
        main_func_page.wait_order_popup()
        main_func_page.click_cancel_button()
        assert main_func_page.check_close_order_pop_up()
