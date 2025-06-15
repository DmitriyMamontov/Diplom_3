from selenium.webdriver.common.by import By


class MainLocators:
    ORDER_FEED = (By.CSS_SELECTOR, "a[href='/feed']") # Кнопка Лента заказов
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
    CONSTRUCTOR_MENU = (By.CLASS_NAME, "App_componentContainer__2JC2W")  # Меню Конструктора
    INGREDIENT_FLYR = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']") # Ингридиент Флюрисцентный бургер
    PIC_INGREDIENT_FLYR = (By.CSS_SELECTOR, "a[href='/ingredient/61c0c5a71d1f82001bdaaa6d']") # Иконка ингридиента Флюрисцентный бургер
    BASKET = (By.CSS_SELECTOR, "div.constructor-element.constructor-element_pos_top") # Корзина заказа
    CLOSE_DETAILS = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4 button") # Кнопка закрыть окно с деталями
    NEW_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка зоформить заказ
    DETAILS_WINDOW_CLOSE = (By.CSS_SELECTOR, ".Modal_modal__P3_V5") # Окно с деталями не отображдается
    DETAILS_WINDOW_ACTIVE = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4.Modal_modal__P3_V5") # Окно с деталями отображдается
    ORDER_WINDOW = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4.Modal_modal__P3_V5") # Окно с деталями заказа отображдается
    COUNTER_FLYR = (By.CSS_SELECTOR, "a[href='/ingredient/61c0c5a71d1f82001bdaaa6d'] .counter_counter__num__3nue1") # Счетчик ингридиентов
