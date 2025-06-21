from curl import *
import allure
from helper import *
class TestPasswordRecovery:

    @allure.title("Тест успешного перехода на страницу восстановления пароля")
    def test_go_to_page_forgot_password(self, recovery_password):
        password_page = recovery_password
        assert password_page.get_current_url() == site_forgot_password


    @allure.title("Тест успешного перехода на вторую страницу восстановления")
    def test_go_to_page_reset_password(self, recovery_password):
        password_page = recovery_password
        email = generate_email_data()
        password_page.fill_mail_field(email)
        password_page.click_recovery_button()
        password_page.go_to_reset_page()
        assert password_page.get_current_url() == site_reset_password

    @allure.title("Тест кнопки скрыть/показать пароль")
    def test_password_visibility_toggle_highlights_field(self, recovery_password):
        password_page = recovery_password
        email = generate_email_data()
        password_page.fill_mail_field(email)
        password_page.click_recovery_button()
        password_page.go_to_reset_page()
        password_page.click_eye_icon()
        assert password_page.wait_active_password_field()
