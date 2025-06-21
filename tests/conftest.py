import pytest
from selenium import webdriver
from curl import *
from pages.order_feed_page import FeedPage
from pages.password_page import PasswordPage
from pages.account_page import AccountPage
from locators.account_locators import AccountLocators
from data import *


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture
def recovery_password(driver):
    password_page = PasswordPage(driver)
    password_page.click_personal_account_header_button()
    password_page.click_forgot_password_button()
    return password_page

@pytest.fixture
def login(driver):
    account_page = AccountPage(driver)
    account_page.main_page_loading_wait()
    account_page.click_personal_account_header_button()
    account_page.main_page_loading_wait()
    account_page.fill_credential_email()
    account_page.fill_credential_password()
    account_page.click_button_login()
    return driver
