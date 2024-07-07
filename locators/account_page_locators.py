from selenium.webdriver.common.by import By


class AccountPageLocators:
    BUTTON_HISTORY_PROFILE = (By.XPATH, "//a[text()='История заказов']")  # Ссылка на кнопку "История заказов"
    BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']")  # Кнопка "Сохранить"
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"
    BUTTON_ORDER_HISTORY = (By.XPATH, "//*[contains(@href,'/account/order-history')]")  # Кнопка "История заказов"
    LIST_ORDERS = (
        By.XPATH, '//*[@class[contains(., "OrderHistory_profileList")]]')  # Кнопка список заказов
