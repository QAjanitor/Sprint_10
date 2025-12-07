import pytest

from data import ADDRESSES


class TestTaxiOrderForm:
    def test_open_form_order_six_tariff(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        assert main_func_page.check_block_order_six_tariff()

    @pytest.mark.xfail(reason="Некорректное описание тарифов: сонный и разговорчивый")
    def test_display_icon_i_and_check_text_tariff(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        main_func_page.call_fast_taxi()
        assert main_func_page.check_texts_tariff_in_icons()

    def test_existence_fields_and_button_order_taxi(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        main_func_page.call_fast_taxi()
        assert main_func_page.check_existence_fields_and_button_order_taxi()
