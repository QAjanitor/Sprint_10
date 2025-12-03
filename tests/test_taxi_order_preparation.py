from data import ADDRESSES


class TestTaxiOrderPreparation:
    # def test_route_type_switching_optimal_to_fast(self, main_func_page):
    #     main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
    #     main_func_page.check_block_route_displayed()
    #     assert main_func_page.change_route_type_updates_data()

    def test_route_type_switching_to_custom(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        main_func_page.check_block_route_displayed()
        assert main_func_page.check_activity_tab_in_custom_route_type()