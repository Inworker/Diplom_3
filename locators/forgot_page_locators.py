from selenium.webdriver.common.by import By


class ForgotPageLocators:
    EMAIL_FIELD = (By.XPATH, '*//input[@type = "text"]')  # Поле "Поле email"
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка "Восстановить"
