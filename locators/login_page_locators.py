from selenium.webdriver.common.by import By


class LoginPageLocator:
    #Локаторы
    BUTTON_RESET_PASSWORD = (By.XPATH, "//*[contains(@href,'/forgot-password')]")
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input")
    INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")