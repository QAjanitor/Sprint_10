from time import sleep

from data import ADDRESSES


class TestTaxiOrderForm:
    def test_open_form_order_six_tariff(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        assert main_func_page.check_block_order_six_tariff()