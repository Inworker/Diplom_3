import allure
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step("Нажать на поле 'Пароль'")  # Страница сброса пароля
    def click_frame_password(self):
        frame = self.driver.find_element(*ResetPasswordPageLocators.PASSWORD_FIELD)
        frame.click()

    @allure.step("Нажать на кнопку 'показать/скрыть пароль'")  # Страцница сброса пароля
    def click_frame_password_eyes(self):
        frame = self.driver.find_element(*ResetPasswordPageLocators.EYES_AREA)
        frame.click()

    @allure.step('Получение и возврат атрибута вида "тип" со значением "текст"')  # Страцница сброса пароля
    def get_input_status(self):
        input_status = self.wait_and_find_element(ResetPasswordPageLocators.PASSWORD_FIELD)
        return input_status.get_attribute("type") == 'text'
