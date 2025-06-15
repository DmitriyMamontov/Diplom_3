import allure
import curl
from pages.base_page import BasePage
from locators.main_locators import MainLocators
from locators.password_locators import PasswordLocators

class MainPage(BasePage):

    @allure.step('Ждем загрузки главной')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(PasswordLocators.OVERLAY)

    @allure.step('Нажать на кнопку Лента заказов')
    def click_button_order_feed(self):
        self.main_page_loading_wait()
        self.click_on_element(MainLocators.ORDER_FEED)

    @allure.step("Подождать url ленты заказов")
    def wait_order_feed_page(self):
        self.main_page_loading_wait()
        self.wait_for_url(curl.order_feed_site)

    @allure.step('Нажать на кнопку Конструктор')
    def click_button_constructor(self):
        self.main_page_loading_wait()
        self.click_on_element(MainLocators.CONSTRUCTOR)

    @allure.step('Нажать на кнопку Заказа')
    def click_button_new_order(self):
        self.main_page_loading_wait()
        self.click_on_element(MainLocators.NEW_ORDER_BUTTON)

    @allure.step('Подождать меню Конструктор')
    def wait_menu_constructor(self):
        self.main_page_loading_wait()
        return self.wait_for_element(MainLocators.CONSTRUCTOR_MENU)

    @allure.step('Подождать видимость всплывающего окна с деталями')
    def wait_details_window(self):
        return self.wait_for_element(MainLocators.DETAILS_WINDOW_ACTIVE)

    @allure.step('Подождать видимость всплывающего окна с оформленным заказом')
    def wait_order_window(self):
        return self.wait_for_element(MainLocators.ORDER_WINDOW)

    @allure.step('Нажать на ингридиент')
    def click_ingredient(self):
        self.main_page_loading_wait()
        self.click_on_element(MainLocators.INGREDIENT_FLYR)

    @allure.step('Закрыть окно с деталями')
    def click_close_details(self):
        self.main_page_loading_wait()
        self.click_on_element(MainLocators.CLOSE_DETAILS)

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_for_element(MainLocators.PIC_INGREDIENT_FLYR)
        basket = self.wait_for_element(MainLocators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('Подождать чтобы всплывающее окно не отображалось')
    def wait_details_window_close(self):
        return self.wait_for_element(MainLocators.DETAILS_WINDOW_CLOSE)

    @allure.step("Получить содержимое каунтера")
    def get_quantity_counter(self):
        return self.get_quantity_on_element(MainLocators.COUNTER_FLYR)




