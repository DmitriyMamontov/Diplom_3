import allure
import curl
from pages.base_page import BasePage
from locators.password_locators import PasswordLocators
from data import *

class PasswordPage(BasePage):

    @allure.step('Ждем загрузки главной')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(PasswordLocators.OVERLAY)

    @allure.step("Нажать на кнопку личный кабинет в шапке")
    def click_personal_account_header_button(self):
        self.main_page_loading_wait()
        self.click_on_element(PasswordLocators.PERSONAL_ACCOUNT)

    @allure.step("Нажать на кнопку восстановить пароль")
    def click_forgot_password_button(self):
        self.main_page_loading_wait()
        self.click_on_element(PasswordLocators.FORGOT_PASSWORD)

    @allure.step("Заполнить поле Email, на странице восстановления пароля")
    def fill_mail_field(self, email):
        self.main_page_loading_wait()
        self.click_on_element(PasswordLocators.RECOVERY_EMAIL_FIELD)
        self.send_keys_to_input(PasswordLocators.RECOVERY_EMAIL_FIELD, email)

    @allure.step("Нажать на кнопку восстановить")
    def click_recovery_button(self):
        self.main_page_loading_wait()
        self.click_on_element(PasswordLocators.RECOVERY_PASSWORD)

    @allure.step("Подождать перехода на 2 страницу восстановления пароля")
    def go_to_reset_page(self):
        self.main_page_loading_wait()
        self.wait_for_url(curl.site_reset_password)

    @allure.step("Нажать на иконку глаза через JS")
    def click_eye_icon(self):
        self.main_page_loading_wait()
        self.js_click(PasswordLocators.EYE_ICON)

    @allure.step("Подождать пока поле пароль станет активным")
    def wait_active_password_field(self):
        return self.wait_active_field(PasswordLocators.ACTIVE_PASSWORD_FIELD)


