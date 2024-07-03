import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

from pages.base_page import BasePage


class TestAccountPage:
    @allure.title("Авторизация пользователя в аккуаунте")
    def test_login_account(self, data_new3, driver_double):
        # Регистрация пользователя и авторизация
        payload = data_new3
        login = BasePage(driver_double)
        login.click_button_login_account()
        login.enter_field_Email(payload["email"])
        login.enter_field_password(payload["password"])
        login.click_button_enter()
        # login.wait_presence_of_element_located(BasePage.BUTTON_ACCOUNT)
        time.sleep(1)  # тут пока не смог сделать ожидание
        login.click(BasePage.BUTTON_ACCOUNT)
        login.wait_and_find_element(BasePage.BUTTON_SAVE)
        assert login.get_answer(BasePage.BUTTON_SAVE) == "Сохранить"

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_orders(self, data_new3, driver_double):
        payload = data_new3
        login = BasePage(driver_double)
        login.click_button_login_account()
        login.enter_field_Email(payload["email"])
        login.enter_field_password(payload["password"])
        login.click_button_enter()
        time.sleep(1)  # тут пока не смог сделать ожидание
        login.click(BasePage.BUTTON_ACCOUNT)
        login.wait_and_find_element(BasePage.BUTTON_SAVE)
        login.click(BasePage.BUTTON_HISTORY_PROFILE)
        # time.sleep(2)  # тут пока не смог сделать ожидание
        #
        # ul = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(BasePage.BUTTON_ORDER_HISTORY))
        # order_list = login.get_order_list()
        # assert order_list is None
        # assert len(order_list) == 0
        # assert True
        assert login.get_current_url() == "https://stellarburgers.nomoreparties.site/account/order-history"

    @allure.title("Выход из личного кабинета")
    def test_exit_user_account(self, data_new3, driver_double):
        payload = data_new3
        login = BasePage(driver_double)
        login.click_button_login_account()
        login.enter_field_Email(payload["email"])
        login.enter_field_password(payload["password"])
        login.click_button_enter()
        time.sleep(1)  # тут пока не смог сделать ожидание
        login.click(BasePage.BUTTON_ACCOUNT)
        login.wait_and_find_element(BasePage.BUTTON_SAVE)
        login.click(BasePage.BUTTON_EXIT)
        assert login.wait_active_element(BasePage.BUTTON_ENTER)
