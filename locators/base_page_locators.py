from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//a/p[text()='Конструктор']")  # Кнопка "Конструктор"
    BUTTON_LIST_ORDER = (By.XPATH, "//a/p[text()='Лента Заказов']")  # Кнопка "Лента заказов"
    FIRST_INGREDIENT_BULKA = (By.XPATH, "*//ul[1]/a[1]")  # 1 булка
    TITLE_DETAILS_INGREDIENT = (By.XPATH, "//*//h2[text()='Детали ингредиента']")  # Заголовок "Детали ингредиента"
    BUTTON_CLOSE = (
        By.XPATH,
        '*//section//button[@type = "button"]')  # Кнопка "закрыть"
    KORZINA = (By.XPATH, '*//section[2]/ul')  # Объект корзина
    COUNT_INGREDIENT = (By.XPATH, "*//ul[1]//p[@class = 'counter_counter__num__3nue1']")  # Счетчик ингредиентов
    BUTTON_CREATE_ORDER = (By.XPATH, '*//button[text() = "Оформить заказ"]')  # Кнопка "оформить заказ"
    TITLE_ORDER_IN_PROCESS = (
        By.XPATH, '*//p[text() = "Ваш заказ начали готовить"]')  # Заголовок "Ваш заказ начали готовить"
    ID_ORDER = (By.XPATH,
                '//h2[contains(@class, "Modal_modal__title_shadow")]')  # Номер заказа
    LAST_ORDER_LENTA = (By.XPATH, "//ul//a//p[@class = 'text text_type_digits-default']")  # Последний заказ в списке
    BUTTON_ACCOUNT = (By.XPATH, "//*[contains(@href,'/account')]")  # Кнопка "Личный кабинет"
