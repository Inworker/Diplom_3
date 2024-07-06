from selenium.webdriver.common.by import By


class ForgotPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")  # Поле "Поле email"
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка "Восстановить"
