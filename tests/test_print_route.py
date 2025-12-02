from data import ADDRESSES


class TestPrintRoute:
    def test_two_dots_displayed_success(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        assert main_func_page.check_points_in_map(ADDRESSES)

    def test_block_route_displayed_success(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        assert main_func_page.check_block_route_displayed()

    def test_free_block_route_displayed_success(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[0])
        assert main_func_page.check_free_block_route_text_displayed()