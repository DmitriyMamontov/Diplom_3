import allure
import curl
from data import *
from pages.base_page import BasePage
from locators.password_locators import PasswordLocators
from locators.account_locators import AccountLocators
class AccountPage(BasePage):

    @allure.step('Ждем загрузки главной')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(PasswordLocators.OVERLAY)

    @allure.step("Нажать на кнопку личный кабинет в шапке")
    def click_personal_account_header_button(self):
        self.main_page_loading_wait()
        self.click_on_element(AccountLocators.PERSONAL_ACCOUNT)

    @allure.step("Подождать url Истории заказов")
    def wait_history_orders_page(self):
        self.main_page_loading_wait()
        self.wait_for_url(curl.history_orders)

    @allure.step("Подождать url вход в аккаунт")
    def wait_account_page(self):
        self.main_page_loading_wait()
        self.wait_for_url(curl.account_site)

    @allure.step("Открыть вкладку история заказов")
    def click_history_orders(self):
        self.main_page_loading_wait()
        self.js_click(AccountLocators.HISTORY_ORDERS)

    @allure.step("Выйти из аккаунта через JS")
    def click_exit_from_account(self):
        self.main_page_loading_wait()
        self.js_click(AccountLocators.EXIT_BUTTON)

    @allure.step("Подождать url выход из аккаунта")
    def wait_exit_account_page(self):
        self.main_page_loading_wait()
        self.wait_for_url(curl.login_endpoint)

    @allure.step("Заполнить поле email")
    def fill_credential_email(self):
        self.main_page_loading_wait()
        self.send_keys_to_input(AccountLocators.EMAIL, Credentials.email)

    @allure.step("Заполнить поле пароль")
    def fill_credential_password(self):
        self.main_page_loading_wait()
        self.send_keys_to_input(AccountLocators.PASSWORD, Credentials.password)

    @allure.step("Нажать кнопку войти")
    def click_button_login(self):
        self.main_page_loading_wait()
        self.click_on_element(AccountLocators.LOG_BUTTON)