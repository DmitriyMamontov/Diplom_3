from pages.order_feed_page import FeedPage
import allure
class TestFeed:

    @allure.title("Тест открытия окна с деталями заказа")
    def test_open_details_order(self, login):
        feed = FeedPage(login)
        feed.click_button_order_feed()
        feed.click_order()
        assert feed.wait_details_order_window()

    @allure.title("Тест заказ пользователя из истории заказов, есть на ленте заказов")
    def test_id_user_order_in_order_feed(self, login):
        feed = FeedPage(login)
        feed.put_ingredient_into_basket()
        feed.click_button_new_order()
        feed.wait_details_order_window()
        order_id = feed.get_order_id_from_confirmation()
        formatted_order_id = f"#0{order_id}"
        feed.click_close_details()
        feed.click_button_order_feed()
        feed.get_order_id_in_progress_list()
        order_in_feed = feed.get_order_id_in_progress_list()
        assert formatted_order_id == order_in_feed


    @allure.title("Тест счетчик всех заказов увеличивается при оформлении нового заказа")
    def test_counter_completed_orders_increasing(self, login):
        feed = FeedPage(login)
        feed.put_ingredient_into_basket()
        feed.click_button_new_order()
        feed.wait_details_order_window()
        order_id = feed.get_order_id_from_confirmation()
        feed.click_close_details()
        feed.click_button_order_feed()
        feed.get_quantity_completed_orders()
        quantity = feed.get_quantity_completed_orders()
        assert order_id == quantity

    @allure.title("Тест счетчик всех заказов сделанных за сегодня увеличивается при оформлении нового заказа")
    def test_counter_completed_orders_increasing(self, login):
        feed = FeedPage(login)
        feed.click_button_order_feed()
        feed.get_count_orders_completed_today()
        quantity_orders_completed_today = feed.get_count_orders_completed_today()
        feed.click_button_constructor()
        feed.put_ingredient_into_basket()
        feed.click_button_new_order()
        feed.wait_details_order_window()
        feed.click_close_details()
        feed.click_button_order_feed()
        feed.get_count_orders_completed_today()
        quantity_update = feed.get_count_orders_completed_today()
        assert quantity_update == quantity_orders_completed_today + 1

    @allure.title("Тест номер нового заказа отображается на экране В работе")
    def test_order_in_window_at_work(self, login):
        feed = FeedPage(login)
        feed.put_ingredient_into_basket()
        feed.click_button_new_order()
        feed.wait_details_order_window()
        order_id = feed.get_order_id_from_confirmation()
        formatted_order_id = f"0{order_id}"
        feed.click_close_details()
        feed.click_button_order_feed()
        feed.get_order_in_window_work()
        id_at_work = feed.get_order_in_window_work()
        assert formatted_order_id == id_at_work