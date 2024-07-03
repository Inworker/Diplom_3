import time

import allure
from data import Urls
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage
from pages.forgot_page import ForgotPage
from pages.loginPage import LoginPage

from pages.reset_password_page import ResetPasswordPage


class TestResetPasswordPage:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_get_reset_password_page(self, driver_double):
        # reset_password = BasePage(driver_double)
        # #Главная страница
        # reset_password.click_button_login_account() #Нажал на кнопку "Личный кабинет"
        # #Страница логина
        # reset_password.click_button_reset_password() # Нажал на кнопку "С
        # assert reset_password.get_current_url() == data.Urls.HOME_PAGE + data.Urls.FORGOT_PASSWORD_END_POINT

        base_page = BasePage(driver_double)
        #Главная страница
        base_page.click_button_login_account() #Нажал на кнопку "Личный кабинет"
        #Страница логина
        login_page = LoginPage(driver_double)
        login_page.click_button_reset_password() # Нажал на кнопку "С
        assert base_page.get_current_url() == Urls.HOME_PAGE + Urls.FORGOT_PASSWORD_END_POINT


    @allure.title("ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_reset(self, driver_double):
        base_page = BasePage(driver_double)
        #Главная страница
        base_page.click_button_login_account()
        #Страница логина
        login_page = LoginPage(driver_double)
        login_page.click_button_reset_password()
        #Страница forgotpage
        forgot_page = ForgotPage(driver_double)
        forgot_page.enter_email_field()
        forgot_page.click_enter_button_restore()

        #Базовый метод
        base_page.wait_for_url_changes_restore()
        assert base_page.get_current_url() == Urls.HOME_PAGE + Urls.RESET_PASSWORD_END_POINT

    @allure.title("Активность поля пароль по кнопке показать/скрыть")
    def test_active_field_password(self, driver_double):
        base_page = BasePage(driver_double)
        #Базовая страница
        base_page.click_button_login_account()
        #Страница логина
        login_page = LoginPage(driver_double)
        login_page.click_button_reset_password()

        #Страница восстановления
        forgot_page = ForgotPage(driver_double)
        forgot_page.enter_email_field()
        forgot_page.click_enter_button_restore()

        #базовый метод
        base_page.wait_for_url_changes_restore()
        #Страница сброса пароля
        reset_page = ResetPasswordPage(driver_double)
        hidden = reset_page.get_input_status()
        base_page.wait_presence_of_element_located(ResetPasswordPageLocators.EYES_AREA)
        # Нажимаем на поле пароля
        reset_page.click_frame_password_eyes()
        # Проверяем состояние поля пароля после клика (должно быть отображенным)
        show = reset_page.get_input_status()
        # Добавляем окончательное утверждение
        assert hidden == False and show == True, "Неправильное состояние поля пароля"


