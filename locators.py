from selenium.webdriver.common.by import By


class Locators:
    INPUT_ADDRESS_FROM = (By.ID, "from")
    INPUT_ADDRESS_TO = (By.ID, "to")
    POINTS = (By.CSS_SELECTOR, ".ymaps-2-1-79-route-pin__text")  # todo при выполнении проверок посмотреть в ТГК "Избранное"
    BLOCK_ROUTE = (By.CSS_SELECTOR, '.type-picker.shown')
    RESULT_TEXT_FREE_CAR_AND_0_TIME = (By.XPATH, "//div[contains(.,'Авто Бесплатно') and contains(.,'В пути 0 мин.')]")
    OPTIMAL_BUTTON = (By.XPATH, "//div[contains(@class, 'mode') and .='Оптимальный']")
    FAST_BUTTON = (By.XPATH, "//div[contains(@class, 'mode') and .='Быстрый']")
    CUSTOM_BUTTON = (By.XPATH, "//div[contains(@class, 'mode') and .='Свой']")
    TYPES = (By.CSS_SELECTOR, '.types-container .type')
    TYPE_ACTIVE_TAB = (By.CSS_SELECTOR, '.type.active')
    RESULT_TEXT = (By.CSS_SELECTOR, ".results-text .text")
    RESULT_TEXT_DURATION = (By.CSS_SELECTOR, ".results-text .duration")
    DRIVE_TYPES = (By.CSS_SELECTOR, ".types-container .type")
    # DRIVE_TYPES = (By.CSS_SELECTOR, ".types-container .type.active")
    TAXI_CALL_BUTTON = (By.XPATH, "//button[.='Вызвать такси']")
    BOOK_A_CAR_BUTTON = (By.XPATH, "//button[.='Забронировать']")
    FORM_ORDER_SIX_TARIFF = (By.CLASS_NAME, 'tariff-picker shown')
    PHONE = (By.XPATH, "//div[@class='np-text' and .='Телефон']")
    PAYMENT = (By.XPATH, "//div[@class='pp-text' and .='Способ оплаты']")
    COMMENT = (By.XPATH, "//label[@class='label' and .='Комментарий водителю...']")
    REQUIREMENTS = (By.XPATH, "//div[@class='reqs-head' and .='Требования к заказу']")