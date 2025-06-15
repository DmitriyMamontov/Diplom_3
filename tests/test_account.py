from pages.account_page import AccountPage
from curl import *
import allure
class TestAccount:

    @allure.title("Тест успешного перехода на страницу личного кабинета")
    def test_go_to_page_account(self, login):
        account = AccountPage(login)
        account.click_personal_account_header_button()
        account.wait_account_page()
        assert account.get_current_url() == account_site

    @allure.title("Тест успешного перехода к истории заказов")
    def test_go_to_history_orders(self, login):
        account = AccountPage(login)
        account.click_personal_account_header_button()
        account.click_history_orders()
        account.wait_history_orders_page()
        assert account.get_current_url() == history_orders

    @allure.title("Тест успешного выхода из аккаунта")
    def test_exit_account(self, login):
        account = AccountPage(login)
        account.click_personal_account_header_button()
        account.click_exit_from_account()
        account.wait_exit_account_page()
        assert account.get_current_url() == login_endpoint