from selenium.webdriver.common.by import By


class PasswordLocators:
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "a[href='/forgot-password']") # Кнопка забыли пароль
    RECOVERY_PASSWORD = (By.XPATH, "//button[text()='Восстановить']") # Кнопка восстановить
    RECOVERY_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле Email для восстановления
    SAVE_NEW_PASSWORD = (By.XPATH, "//button[text()='Сохранить']") # Кнопка сохранить пароль
    NEW_PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # Поле Пароль для восстановления
    EYE_ICON = (By.CSS_SELECTOR, ".input__icon-action") # Иконка глаза
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div") # Невидимый оверлей
    ACTIVE_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='text'][name='Введите новый пароль']") # Активное поле с паролем