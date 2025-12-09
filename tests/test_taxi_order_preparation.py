import allure


class TestTaxiOrderPreparation:
    @allure.title("Тест: Переключение типа маршрута с оптимального на быстрый")
    @allure.description("Проверка корректного обновления данных при смене типа маршрута")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("маршрут", "переключение", "функциональность")
    def test_route_type_switching_optimal_to_fast(self, main_func_page_filled_addresses):
        with allure.step("Шаг 1: Проверка отображения блока маршрута"):
            main_func_page_filled_addresses.check_block_route_displayed()

        with allure.step("Шаг 2: Проверка обновления данных при переключении типа маршрута"):
            result = main_func_page_filled_addresses.check_change_route_type_updates_data()

        with allure.step("Шаг 3: Проверка результата теста"):
            allure.attach(
                f"Результат проверки: {result}",
                name="Test Result",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Данные не обновились при переключении типа маршрута"

    @allure.title("Тест: Переключение типа маршрута на кастомный")
    @allure.description("Проверка активности вкладок в кастомном типе маршрута")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("маршрут", "кастомный", "активность")
    def test_route_type_switching_to_custom(self, main_func_page_filled_addresses):
        with allure.step("Шаг 1: Проверка отображения блока маршрута"):
            main_func_page_filled_addresses.check_block_route_displayed()

        with allure.step("Шаг 2: Проверка активности вкладок в кастомном маршруте"):
            result = main_func_page_filled_addresses.check_activity_tab_in_custom_route_type()

        with allure.step("Шаг 3: Проверка результата теста"):
            allure.attach(
                f"Все вкладки активны: {result}",
                name="Test Result",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Не все вкладки активны в кастомном маршруте"

    @allure.title("Тест: Активность кнопки вызова такси при быстром маршруте")
    @allure.description("Проверка, что кнопка вызова такси активна при выборе быстрого маршрута")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("кнопка", "активность", "быстрый маршрут")
    def test_fast_route_has_order_taxi_button_active(self, main_func_page_filled_addresses):
        with allure.step("Шаг 1: Проверка отображения блока маршрута"):
            main_func_page_filled_addresses.check_block_route_displayed()

        with allure.step("Шаг 2: Проверка активности кнопки вызова такси"):
            result = main_func_page_filled_addresses.check_button_call_taxi_is_active()

        with allure.step("Шаг 3: Проверка результата теста"):
            allure.attach(
                f"Кнопка вызова такси активна: {result}",
                name="Test Result",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Кнопка вызова такси не активна при быстром маршруте"

    @allure.title("Тест: Активность кнопки бронирования при кастомном маршруте с поездкой")
    @allure.description("Проверка активности кнопки 'Забронировать' при выборе кастомного маршрута с поездкой")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("бронирование", "кастомный маршрут", "активность")
    def test_custom_route_with_drive_has_book_button_active(self, main_func_page_filled_addresses):
        with allure.step("Шаг 1: Проверка отображения блока маршрута"):
            main_func_page_filled_addresses.check_block_route_displayed()

        with allure.step("Шаг 2: Проверка активности кнопки бронирования"):
            result = main_func_page_filled_addresses.check_book_a_car_button_is_active()

        with allure.step("Шаг 3: Проверка результата теста"):
            allure.attach(
                f"Кнопка бронирования активна: {result}",
                name="Test Result",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Кнопка бронирования не активна при кастомном маршруте с поездкой"
