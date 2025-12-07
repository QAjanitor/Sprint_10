import pytest
import allure


class TestTaxiOrderForm:
    @allure.title("Тест: Открытие формы заказа с шестью тарифами")
    @allure.description("Проверка корректного отображения формы заказа с шестью тарифами")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("форма заказа", "тарифы", "отображение")
    def test_open_form_order_six_tariff(self, main_func_page_filled_addresses):
        with allure.step("Шаг 1: Проверка отображения блока с шестью тарифами"):
            result = main_func_page_filled_addresses.check_block_order_six_tariff()
            allure.attach(
                f"Форма заказа с шестью тарифами отображается: {result}",
                name="Six Tariffs Form Check",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Форма заказа с шестью тарифами не отображается"

    @pytest.mark.xfail(reason="Некорректное описание тарифов: сонный и разговорчивый")
    @allure.title("Тест: Отображение иконки 'i' и проверка текста тарифов")
    @allure.description("Проверка корректности описаний тарифов при наведении на иконку информации")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("иконка", "описание тарифов", "тултип")
    def test_display_icon_i_and_check_text_tariff(self, main_func_page_filled_addresses):
        with allure.step("Шаг 1: Вызов быстрого такси"):
            main_func_page_filled_addresses.call_fast_taxi()

        with allure.step("Шаг 2: Проверка текстов тарифов в иконках"):
            result = main_func_page_filled_addresses.check_texts_tariff_in_icons()
            allure.attach(
                f"Тексты тарифов корректны: {result}",
                name="Tariff Texts Check",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Тексты тарифов не соответствуют ожидаемым описаниям"

    @allure.title("Тест: Наличие полей формы и кнопки заказа такси")
    @allure.description("Проверка наличия всех необходимых элементов формы заказа такси")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("форма", "поля ввода", "кнопка заказа")
    def test_existence_fields_and_button_order_taxi(self, main_func_page_filled_addresses):
        with allure.step("Шаг 1: Вызов быстрого такси"):
            main_func_page_filled_addresses.call_fast_taxi()

        with allure.step("Шаг 2: Проверка наличия полей формы и кнопки заказа"):
            result = main_func_page_filled_addresses.check_existence_fields_and_button_order_taxi()
            allure.attach(
                f"Все поля формы и кнопка заказа присутствуют: {result}",
                name="Form Elements Existence",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Не все необходимые элементы формы заказа присутствуют на странице"
