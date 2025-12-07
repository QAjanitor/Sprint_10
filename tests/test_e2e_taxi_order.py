from data import ADDRESSES


class TestE2ETaxiOrder:
    def test_select_work_tariff_with_laptop_table_option(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        main_func_page.call_fast_taxi()
        main_func_page.select_work_tariff_and_laptop_with_click_order_taxi_button()
        assert main_func_page.check_waiting_pop_up_success_order()