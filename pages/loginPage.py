
import allure

from locators.login_page_locators import LoginPageLocator
from pages.base_page import BasePage


class LoginPage(BasePage):


    # Страница логина
    @allure.step("Нажать на cсылку 'Восстановить пароль'")  # Страцница логина
    def click_button_reset_password(self):
        button = self.driver.find_element(*LoginPageLocator.BUTTON_RESET_PASSWORD)
        button.click()

    @allure.step('Заполнить поле "Email"')
    def enter_field_Email(self, email):
        field = self.driver.find_element(*LoginPageLocator.INPUT_EMAIL)
        field.send_keys(email)



    @allure.step('Заполнить поле "Пароль"')
    def enter_field_password(self, password):
        field = self.driver.find_element(*LoginPageLocator.INPUT_PASSWORD)
        field.send_keys(password)


    @allure.step('Нажать на кнопку "Войти"')
    def click_button_enter(self):
        button = self.driver.find_element(*LoginPageLocator.BUTTON_ENTER)
        button.click()

