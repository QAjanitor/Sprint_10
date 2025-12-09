from data import ADDRESSES
import allure


class TestRouteBlockRender:
    @allure.title("Тест: Отображение блока маршрута при заполнении адресов")
    @allure.description("Проверка корректного отображения блока маршрута после ввода адресов")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("блок маршрута", "адреса", "отображение")
    def test_block_route_displayed_success(self, main_func_page):
        with allure.step("Шаг 1: Заполнение полей адресов"):
            allure.attach(
                f"Адрес отправления: {ADDRESSES[0]}",
                name="From Address",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                f"Адрес назначения: {ADDRESSES[1]}",
                name="To Address",
                attachment_type=allure.attachment_type.TEXT
            )
            main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[1])

        with allure.step("Шаг 2: Проверка отображения блока маршрута"):
            result = main_func_page.check_block_route_displayed()
            allure.attach(
                f"Блок маршрута отображается: {result}",
                name="Route Block Display Check",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Блок маршрута не отображается после заполнения адресов"

    @allure.title("Тест: Отображение текста свободного блока маршрута при одинаковых адресах")
    @allure.description("Проверка отображения специального текста при вводе одинаковых адресов")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("свободный блок", "одинаковые адреса", "специальный текст")
    def test_free_block_route_displayed_success(self, main_func_page):
        with allure.step("Шаг 1: Заполнение одинаковых адресов"):
            allure.attach(
                f"Адрес отправления и назначения: {ADDRESSES[0]}",
                name="Same Address",
                attachment_type=allure.attachment_type.TEXT
            )
            main_func_page.fill_addresses(ADDRESSES[0], ADDRESSES[0])

        with allure.step("Шаг 2: Проверка отображения текста свободного блока маршрута"):
            result = main_func_page.check_free_block_route_text_displayed()
            allure.attach(
                f"Текст свободного блока отображается: {result}",
                name="Free Block Text Display Check",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result, "Текст свободного блока маршрута не отображается при одинаковых адресах"
