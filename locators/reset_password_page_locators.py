from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")  # Поле ввода "Введите новый пароль"
    EYES_AREA = (By.XPATH, '//*[@class[contains(., "input__icon")]]')  # Иконка скрыть/показать пароль
