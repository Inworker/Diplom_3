import allure
import data
from locators.forgot_page_locators import ForgotPageLocators
from pages.base_page import BasePage


class ForgotPage(BasePage):



    @allure.step("Ввести Email")  # Страцница сброса пароля
    def enter_email_field(self):
        field = self.driver.find_element(*ForgotPageLocators.EMAIL_FIELD)
        field.send_keys(data.FakeData.fake_email)

    @allure.step("Нажать на кнопку 'Восстановить'")  # Страцница сброса пароля
    def click_enter_button_restore(self):
        button = self.driver.find_element(*ForgotPageLocators.RESTORE_BUTTON)
        button.click()
