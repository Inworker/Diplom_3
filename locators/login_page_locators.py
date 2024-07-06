from selenium.webdriver.common.by import By


class LoginPageLocator:
    BUTTON_RESET_PASSWORD = (By.XPATH, "//*[contains(@href,'/forgot-password')]")  # Кнопка сбросить пароль
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input")  # Поле ввода "Email"
    INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input")  # Поле ввода "Пароль"
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
