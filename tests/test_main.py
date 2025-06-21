from pages.main_page import MainPage
from curl import *
import allure
class TestMain:

    @allure.title("Тест успешного перехода на страницу ленты заказов")
    def test_page_feed_orders(self, login):
        main = MainPage(login)
        main.click_button_order_feed()
        main.wait_order_feed_page()
        assert main.get_current_url() == order_feed_site

    @allure.title("Тест успешного перехода к конструктору")
    def test_go_to_constructor(self, login):
        main = MainPage(login)
        main.click_button_order_feed()
        main.wait_order_feed_page()
        main.click_button_constructor()
        assert main.wait_menu_constructor()

    @allure.title("Тест открытия окна с деталями ингридиента")
    def test_open_details(self, login):
        main = MainPage(login)
        main.click_ingredient()
        assert main.wait_details_window()

    @allure.title("Тест закрытия окна с деталями ингридиента")
    def test_close_details(self, login):
        main = MainPage(login)
        main.click_ingredient()
        main.click_close_details()
        assert main.wait_details_window_close()

    @allure.title("Тест добавления ингридиента в заказ")
    def test_add_ingredient_in_order(self, login):
        main = MainPage(login)
        main.put_ingredient_into_basket()
        assert main.get_quantity_counter() == 2

    @allure.title("Тест оформления заказа")
    def test_order_check(self, login):
        main = MainPage(login)
        main.put_ingredient_into_basket()
        main.click_button_new_order()
        assert main.wait_order_window()
