from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")  # Поле ввода "Введите новый пароль"
    EYES_AREA = (By.XPATH, "//div[@class='input__icon input__icon-action']")  # Иконка скрыть/показать пароль
