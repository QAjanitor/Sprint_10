import pytest


class TestTaxiOrderForm:
    def test_open_form_order_six_tariff(self, main_func_page_filled_addresses):
        assert main_func_page_filled_addresses.check_block_order_six_tariff()

    @pytest.mark.xfail(reason="Некорректное описание тарифов: сонный и разговорчивый")
    def test_display_icon_i_and_check_text_tariff(self, main_func_page_filled_addresses):
        main_func_page_filled_addresses.call_fast_taxi()
        assert main_func_page_filled_addresses.check_texts_tariff_in_icons()

    def test_existence_fields_and_button_order_taxi(self, main_func_page_filled_addresses):
        main_func_page_filled_addresses.call_fast_taxi()
        assert main_func_page_filled_addresses.check_existence_fields_and_button_order_taxi()
