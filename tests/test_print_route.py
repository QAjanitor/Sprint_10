from data import ADDRESSES


class TestPrintRoute:
    def test_two_dots_displayed_success(self, main_func_page):
        main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])
        assert main_func_page.check_points_in_map(ADDRESSES)

