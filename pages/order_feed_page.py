from locators.order_feed_locators import FeedLocators
import allure
from pages.base_page import BasePage
from locators.main_locators import MainLocators
from locators.password_locators import PasswordLocators

class FeedPage(BasePage):

    @allure.step('Ждем загрузки главной')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(PasswordLocators.OVERLAY)

    @allure.step('Нажать на кнопку Лента заказов')
    def click_button_order_feed(self):
        self.main_page_loading_wait()
        self.click_on_element(MainLocators.ORDER_FEED)

    @allure.step('Нажать на заказ')
    def click_order(self):
        self.main_page_loading_wait()
        self.click_on_element(FeedLocators.ORDERS)

    @allure.step('Подождать видимость всплывающего окна с заказом')
    def wait_details_order_window(self):
        self.main_page_loading_wait()
        return self.wait_for_element(FeedLocators.DETAILS_ORDER_WINDOW)

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_for_element(MainLocators.PIC_INGREDIENT_FLYR)
        basket = self.wait_for_element(MainLocators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('Нажать на кнопку Заказа')
    def click_button_new_order(self):
        self.main_page_loading_wait()
        self.click_on_element(MainLocators.NEW_ORDER_BUTTON)

    @allure.step('Получить id из окна оформленного заказа')
    def get_order_id_from_confirmation(self):
        self.main_page_loading_wait()
        result = self.get_text_on_element(FeedLocators.ORDER_CONFIRMATION_ID)
        return result

    @allure.step('Получить id из ленты заказов')
    def get_order_id_in_progress_list(self):
        self.wait_for_element(FeedLocators.ORDERS_AT_FEED)
        result = self.get_text_on_element(FeedLocators.ORDERS_AT_FEED)
        return result

    @allure.step('Закрыть окно с деталями')
    def click_close_details(self):
        self.main_page_loading_wait()
        self.click_on_element(MainLocators.CLOSE_DETAILS)

    @allure.step('Получить id из экрана Выполнено за все время')
    def get_quantity_completed_orders(self):
        self.wait_for_element(FeedLocators.ORDERS_COMPLETED)
        result = self.get_text_on_element(FeedLocators.ORDERS_COMPLETED)
        return result

    @allure.step('Получить id из экрана Выполнено за сегодня')
    def get_count_orders_completed_today(self):
        self.wait_for_element(FeedLocators.ORDER_FEED_COMPLETED_TODAY_COUNT)
        result = self.get_text_on_element(FeedLocators.ORDER_FEED_COMPLETED_TODAY_COUNT)
        return int(result)

    @allure.step('Нажать на кнопку Конструктор')
    def click_button_constructor(self):
        self.main_page_loading_wait()
        self.click_on_element(MainLocators.CONSTRUCTOR)

    @allure.step('Получить id из экрана В работе')
    def get_order_in_window_work(self):
        self.wait_for_element(FeedLocators.ORDERS_AT_WORK)
        result = self.get_text_on_element(FeedLocators.ORDERS_AT_WORK)
        return result