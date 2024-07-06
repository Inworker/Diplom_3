import allure
from data import Urls
from pages.base_page import BasePage
from pages.forgot_page import ForgotPage
from pages.loginPage import LoginPage
from pages.reset_password_page import ResetPasswordPage


class TestResetPasswordPage:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_get_reset_password_page(self, driver_double):
        base_page = BasePage(driver_double)
        base_page.click_button_login_account()
        login_page = LoginPage(driver_double)
        login_page.click_button_reset_password()
        assert base_page.get_current_url() == Urls.HOME_PAGE + Urls.FORGOT_PASSWORD_END_POINT

    @allure.title("ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_reset(self, driver_double):
        base_page = BasePage(driver_double)
        base_page.click_button_login_account()
        login_page = LoginPage(driver_double)
        login_page.click_button_reset_password()
        forgot_page = ForgotPage(driver_double)
        forgot_page.enter_email_click_restore()
        base_page.wait_for_url_changes_restore()
        assert base_page.get_current_url() == Urls.HOME_PAGE + Urls.RESET_PASSWORD_END_POINT

    @allure.title("Активность поля пароль по кнопке показать/скрыть")
    def test_active_field_password(self, driver_double):
        base_page = BasePage(driver_double)
        base_page.click_button_login_account()
        login_page = LoginPage(driver_double)
        login_page.click_button_reset_password()
        forgot_page = ForgotPage(driver_double)
        forgot_page.enter_email_click_restore()
        base_page.wait_for_url_changes_restore()
        reset_page = ResetPasswordPage(driver_double)
        hidden = reset_page.get_input_status()
        reset_page.wait_icon_eyes()
        reset_page.wait_icon_eyes_clikable()
        reset_page.click_frame_password_eyes()
        show = reset_page.get_input_status()
        assert hidden == False and show == True, "Неправильное состояние поля пароля"
