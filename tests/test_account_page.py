import allure
from locators.login_page_locators import LoginPageLocator
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.loginPage import LoginPage


class TestAccountPage:
    @allure.title("Авторизация пользователя в аккуаунте")
    def test_login_account(self, create_user_data, driver_double):
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        login = LoginPage(driver_double)
        login.enter_login_password(create_user_data)
        basepage.wait_active_create_order_click_account()
        account_page = AccountPage(driver_double)
        account_page.wait_button_save()
        assert account_page.get_text_button_save() == "Сохранить"

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_orders(self, create_user_data, driver_double):
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        login = LoginPage(driver_double)
        login.enter_login_password(create_user_data)
        basepage.wait_active_create_order_click_account()
        account_page = AccountPage(driver_double)
        account_page.wait_button_save_click_history()
        assert basepage.get_current_url() == "https://stellarburgers.nomoreparties.site/account/order-history"

    @allure.title("Выход из личного кабинета")
    def test_exit_user_account(self, create_user_data, driver_double):
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        login = LoginPage(driver_double)
        login.enter_login_password(create_user_data)
        basepage.wait_active_create_order_click_account()
        account_page = AccountPage(driver_double)
        account_page.wait_button_save_click_exit()
        assert basepage.wait_active_element(LoginPageLocator.BUTTON_ENTER)
