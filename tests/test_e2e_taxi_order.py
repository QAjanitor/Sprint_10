import pytest
import allure


class TestE2ETaxiOrder:
    @allure.title("Тест E2E: Выбор рабочего тарифа с опцией столика для ноутбука")
    @allure.description("Полный сквозной тест заказа такси с выбором тарифа и дополнительных опций")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("e2e", "заказ", "тариф", "дополнительные опции")
    def test_select_work_tariff_with_laptop_table_option(self, main_func_page_filled_addresses):
        with allure.step("Шаг 1: Вызов быстрого такси"):
            main_func_page_filled_addresses.call_fast_taxi()

        with allure.step("Шаг 2: Выбор рабочего тарифа и опции столика для ноутбука"):
            main_func_page_filled_addresses.select_work_tariff_and_laptop_with_click_order_taxi_button()

        with allure.step("Шаг 3: Проверка отображения поп-апа ожидания заказа"):
            result1 = main_func_page_filled_addresses.check_waiting_pop_up_waiting_order()
            allure.attach(
                f"Поп-ап ожидания отображается: {result1}",
                name="Popup Display Check",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result1, "Поп-ап ожидания заказа не отображается"

        with allure.step("Шаг 4: Проверка всех элементов в поп-апе ожидания заказа"):
            result2 = main_func_page_filled_addresses.check_all_elements_in_pop_up_waiting_order()
            allure.attach(
                f"Все элементы поп-апа присутствуют: {result2}",
                name="Popup Elements Check",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result2, "Не все элементы отображаются в поп-апе ожидания заказа"

    @allure.title("Тест E2E: Ожидание таймера поиска водителя")
    @allure.description("Проверка процесса поиска водителя и отображения информации о нем")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("e2e", "поиск водителя", "таймер", "информация")
    def test_wait_for_driver_search_timer(self, main_func_page_filled_addresses):
        with allure.step("Шаг 1: Заказ быстрого такси с рабочим тарифом"):
            main_func_page_filled_addresses.order_fast_taxi_work_tariff()

        with allure.step("Шаг 2: Проверка всех элементов в поп-апе успешного заказа"):
            result = main_func_page_filled_addresses.check_all_elements_in_pop_up_success_order()
            allure.attach(
                f"Все элементы успешного заказа присутствуют: {result}",
                name="Success Popup Elements",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Не все элементы отображаются в поп-апе успешного заказа"

    @allure.title("Тест E2E: Сравнение цены в деталях заказа с ценой при выборе тарифа")
    @allure.description("Проверка соответствия цены на разных этапах оформления заказа")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("e2e", "цена", "сравнение", "детали заказа")
    def test_price_in_details_same_in_select_tariff(self, main_func_page_filled_addresses):
        with allure.step("Шаг 1: Заказ такси с запоминанием цены"):
            main_func_page_filled_addresses.order_fast_taxi_work_tariff(True)

        with allure.step("Шаг 2: Сравнение цены в деталях заказа с изначальной ценой"):
            result = main_func_page_filled_addresses.check_comparison_price_in_details_same_in_select_tariff()
            allure.attach(
                f"Цены совпадают: {result}",
                name="Price Comparison Result",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Цена в деталях заказа не совпадает с ценой при выборе тарифа"

    @pytest.mark.xfail(reason="Не работает кнопка 'Отменить' на поп-апе заказа такси")
    @allure.title("Тест E2E: Нажатие кнопки 'Отменить' в поп-апе заказа такси")
    @allure.description("Проверка функциональности отмены заказа через поп-ап")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("e2e", "отмена", "поп-ап", "негативный сценарий")
    def test_click_button_cancel_in_pop_up_order(self, main_func_page_filled_addresses):
        with allure.step("Шаг 1: Заказ быстрого такси с рабочим тарифом"):
            main_func_page_filled_addresses.order_fast_taxi_work_tariff()

        with allure.step("Шаг 2: Нажатие кнопки 'Отменить' в поп-апе заказа"):
            main_func_page_filled_addresses.click_cancel_button()

        with allure.step("Шаг 3: Проверка закрытия поп-апа заказа"):
            result = main_func_page_filled_addresses.check_close_order_pop_up()
            allure.attach(
                f"Поп-ап заказа закрыт: {result}",
                name="Popup Closed Check",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Поп-ап заказа не закрылся после нажатия кнопки 'Отменить'"
