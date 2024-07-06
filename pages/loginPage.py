from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from locators.login_page_locators import LoginPageLocator
from pages.base_page import BasePage


class LoginPage(BasePage):

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

    @allure.step("Заполнить логин и пароль и войти в аккаунт")
    def enter_login_password(self, data_new3):
        payload = data_new3
        self.enter_field_Email(payload["email"])
        self.enter_field_password(payload["password"])
        self.wait_active_element_button_enter()
        self.click_button_enter()

    @allure.step("Подождать, что кнопка Вход активна")
    def wait_active_element_button_enter(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(LoginPageLocator.BUTTON_ENTER))
        return self.driver.find_element(*LoginPageLocator.BUTTON_ENTER)
