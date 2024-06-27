import allure
import data
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestResetPasswordPage:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_get_reset_password_page(self, driver_double):
        reset_password = BasePage(driver_double)
        reset_password.click_button_login_account()
        reset_password.click_button_reset_password()
        assert reset_password.get_current_url() == data.Urls.HOME_PAGE + data.Urls.FORGOT_PASSWORD_END_POINT

    @allure.title("ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_reset(self, driver_double):
        reset_password = BasePage(driver_double)
        reset_password.click_button_login_account()
        reset_password.click_button_reset_password()
        reset_password.enter_email_field()
        reset_password.click_enter_button_restore()
        reset_password.wait_for_url_changes_restore()
        assert reset_password.get_current_url() == data.Urls.HOME_PAGE + data.Urls.RESET_PASSWORD_END_POINT

    @allure.title("Активность поля пароль по кнопке показать/скрыть")
    def test_active_field_password(self, driver_double):
        reset_password = BasePage(driver_double)
        reset_password.click_button_login_account()
        reset_password.click_button_reset_password()
        reset_password.enter_email_field()
        reset_password.click_enter_button_restore()
        reset_password.wait_for_url_changes_restore()
        hidden = reset_password.get_input_status()
        reset_password.click_frame_password()
        show = reset_password.get_input_status()
        assert hidden == False and show == True


