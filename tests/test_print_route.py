from data import ADDRESSES
import allure


class TestPrintRoute:
    @allure.title("Тест: Отображение двух точек на карте")
    @allure.description("Проверка корректного отображения точек маршрута на карте")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("карта", "точки маршрута", "визуализация")
    def test_two_dots_displayed_success(self, main_func_page):
        with allure.step("Шаг 1: Заполнение адресов для построения маршрута"):
            allure.attach(
                f"Адреса для проверки: {ADDRESSES}",
                name="Addresses List",
                attachment_type=allure.attachment_type.TEXT
            )
            main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])

        with allure.step("Шаг 2: Проверка отображения точек на карте"):
            result = main_func_page.check_points_in_map(ADDRESSES)
            allure.attach(
                f"Точки маршрута отображаются на карте: {result}",
                name="Points Display Check",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Точки маршрута не отображаются на карте после ввода адресов"
