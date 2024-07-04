import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

from locators.account_page_locators import AccountPageLocators
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocator
from pages.base_page import BasePage
from pages.loginPage import LoginPage


class TestAccountPage:
    @allure.title("Авторизация пользователя в аккуаунте")
    def test_login_account(self, data_new3, driver_double):
        # Регистрация пользователя и авторизация
        payload = data_new3
        #Сделал экземпляр базовой страницы
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        #Сделал экземпляр страницы логина
        login  = LoginPage(driver_double)
        #Ввел мыло, пароль и нажал enter
        login.enter_field_Email(payload["email"])
        login.enter_field_password(payload["password"])
        basepage.wait_active_element(LoginPageLocator.BUTTON_ENTER)
        login.click_button_enter()
        #Сделал ожидание перехода на базовую страницу
        # basepage.wait_presence_of_element_located(BasePageLocators.BUTTON_CONSTRUCTOR2)
        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)
        # time.sleep(1)  # тут пока не смог сделать ожидание
        basepage.click(BasePageLocators.BUTTON_ACCOUNT)
        #Подождать пока появится кнопка сохранить
        basepage.wait_and_find_element(AccountPageLocators.BUTTON_SAVE)
        assert basepage.get_answer(AccountPageLocators.BUTTON_SAVE) == "Сохранить"

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_orders(self, data_new3, driver_double):
        # Регистрация пользователя и авторизация
        payload = data_new3
        # Сделал экземпляр базовой страницы
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        # Сделал экземпляр страницы логина
        login = LoginPage(driver_double)
        # Ввел мыло, пароль и нажал enter
        login.enter_field_Email(payload["email"])
        login.enter_field_password(payload["password"])
        basepage.wait_active_element(LoginPageLocator.BUTTON_ENTER)
        login.click_button_enter()
        # Сделал ожидание перехода на базовую страницу
        # basepage.wait_presence_of_element_located(BasePageLocators.BUTTON_CONSTRUCTOR2)
        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)
        # time.sleep(1)  # тут пока не смог сделать ожидание
        basepage.click(BasePageLocators.BUTTON_ACCOUNT)
        # Подождать пока появится кнопка сохранить
        basepage.wait_and_find_element(AccountPageLocators.BUTTON_SAVE)

        basepage.click(AccountPageLocators.BUTTON_HISTORY_PROFILE)

        assert login.get_current_url() == "https://stellarburgers.nomoreparties.site/account/order-history"

    @allure.title("Выход из личного кабинета")
    def test_exit_user_account(self, data_new3, driver_double):
        # Регистрация пользователя и авторизация
        payload = data_new3
        # Сделал экземпляр базовой страницы
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        # Сделал экземпляр страницы логина
        login = LoginPage(driver_double)
        # Ввел мыло, пароль и нажал enter
        login.enter_field_Email(payload["email"])
        login.enter_field_password(payload["password"])
        basepage.wait_active_element(LoginPageLocator.BUTTON_ENTER)
        login.click_button_enter()
        # Сделал ожидание перехода на базовую страницу
        # basepage.wait_presence_of_element_located(BasePageLocators.BUTTON_CONSTRUCTOR2)
        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)
        # time.sleep(1)  # тут пока не смог сделать ожидание
        basepage.click(BasePageLocators.BUTTON_ACCOUNT)
        # Подождать пока появится кнопка сохранить
        basepage.wait_and_find_element(AccountPageLocators.BUTTON_SAVE)
        basepage.click(AccountPageLocators.BUTTON_EXIT)
        assert basepage.wait_active_element(LoginPageLocator.BUTTON_ENTER)
