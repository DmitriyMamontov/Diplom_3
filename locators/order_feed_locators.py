from selenium.webdriver.common.by import By

class FeedLocators:
    ORDERS = (By.CSS_SELECTOR, ".OrderHistory_listItem__2x95r") # Заказы на ленте заказов
    DETAILS_ORDER_WINDOW = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4.Modal_modal__P3_V5") # Окно с деталями заказа
    ORDER_CONFIRMATION_ID = (By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq") # Окно оформленного заказа
    ORDERS_AT_WORK = By.XPATH, ".//ul[contains(@class, 'orderListReady')]/li[contains(@class, 'default mb-2')]" # Окно В работе
    ORDERS_AT_FEED = By.XPATH, "//p[starts-with(text(), '#0')]" # ID заказа в ленте заказов
    ORDERS_COMPLETED = By.XPATH, ".//div[contains(@class, 'undefined')]/p[contains(@class, 'OrderFeed_number')]" # Окно выполненных заказов за все время
    ORDER_FEED_COMPLETED_TODAY_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[1]") # Окно выполненных заказов за сегодня
