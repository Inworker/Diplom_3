from selenium.webdriver.common.by import By


class AccountPageLocators:
    BUTTON_HISTORY_PROFILE = (By.XPATH, "//a[text()='История заказов']")
    BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']")
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']")
    BUTTON_ORDER_HISTORY = (By.XPATH, "//*[contains(@href,'/account/order-history')]")
    LIST_ORDERS = (By.XPATH, '//ul[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]')
