from selenium.webdriver.common.by import By


class AccountLocators:
    PERSONAL_ACCOUNT = (By.CSS_SELECTOR, "a[href='/account']")  # Кнопка "Личный кабинет"
    HISTORY_ORDERS = (By.CSS_SELECTOR, "a[href='/account/order-history']")  # Вкладка История заказов
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле ввода Email
    PASSWORD = (By.XPATH, "//input[@type='password']") # Поле ввода Пароля
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка Выйти из аккаунта
    LOG_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"