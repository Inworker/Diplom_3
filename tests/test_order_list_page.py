import time

import allure

from locators.account_page_locators import AccountPageLocators
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocator
from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage
from pages.loginPage import LoginPage


class TestOrdersList:

    @allure.title("если кликнуть на заказ, откроется всплывающее окно с деталями,")
    def test_get_window_details(self, driver_double):
        basepage = BasePage(driver_double)
        basepage.click(BasePageLocators.BUTTON_LIST_ORDER)
        # time.sleep(1)
        basepage.wait_active_element(OrderListPageLocators.FIRST_ORDER)
        basepage.click(OrderListPageLocators.FIRST_ORDER)
        # time.sleep(1)
        basepage.wait_presence_of_element_located(OrderListPageLocators.TITLE_SOSTAV)
        sostav = basepage.get_answer(OrderListPageLocators.TITLE_SOSTAV)
        assert sostav == "Cостав"


    @allure.title("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,")
    def test_get_order_user_page_order_history(self,data_new3, driver_double):
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
        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)
        # time.sleep(1)  # тут пока не смог сделать ожидание
        basepage.drop_ingredient_korzina()
        basepage.click(BasePageLocators.BUTTON_CREATE_ORDER)


        basepage.wait_active_element(BasePageLocators.BUTTON_CLOSE)
        basepage.wait_title_change_not_9999()
        count_order = basepage.get_answer(BasePageLocators.ID_ORDER)
        assert count_order != "9999"
        basepage.click(BasePageLocators.BUTTON_CLOSE)
        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)
        basepage.click(BasePageLocators.BUTTON_ACCOUNT)

        basepage.wait_presence_of_element_located(AccountPageLocators.BUTTON_SAVE)
        basepage.click(AccountPageLocators.BUTTON_HISTORY_PROFILE)
        basepage.wait_presence_of_element_located(OrderListPageLocators.LAST_ORDER_ACCOUNT)
        count_order_account = basepage.get_answer(OrderListPageLocators.LAST_ORDER_ACCOUNT)
        assert count_order in count_order_account
        basepage.click(BasePageLocators.BUTTON_LIST_ORDER)
        basepage.wait_presence_of_element_located(OrderListPageLocators.LAST_ORDER_ACCOUNT)
        order_lenta = basepage.get_answer(OrderListPageLocators.LAST_ORDER_ACCOUNT)

        assert order_lenta == count_order_account




    @allure.title("при создании нового заказа счётчик Выполнено за всё время увеличивается,")
    def test_count_all_time(self, data_new3, driver_double):
        #Тут авторизация пользователя
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
        basepage.wait_presence_of_element_located(LoginPageLocator.BUTTON_RESET_PASSWORD)
        login.click_button_enter()
        # Сделал ожидание перехода на базовую страницу
        # basepage.wait_presence_of_element_located(BasePageLocators.BUTTON_CONSTRUCTOR2)
        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)

        basepage.click(BasePageLocators.BUTTON_LIST_ORDER)

        # time.sleep(3)  # Это надо обыграть как то
        basepage.wait_presence_of_element_located(OrderListPageLocators.COUNT_ALL_ORDERS)
        #Тут получил список заказов за все время
        count_all_orders = basepage.get_answer(OrderListPageLocators.COUNT_ALL_ORDERS)
        # time.sleep(3)

        #тут перешел на страницу конструктора
        basepage.click(BasePageLocators.BUTTON_CONSTRUCTOR)
        # time.sleep(1)
        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)

        basepage.drop_ingredient_korzina()
        basepage.click(BasePageLocators.BUTTON_CREATE_ORDER)

        basepage.wait_active_element(BasePageLocators.BUTTON_CLOSE)
        basepage.wait_title_change_not_9999()
        count_order = basepage.get_answer(BasePageLocators.ID_ORDER)
        assert count_order != "9999"
        basepage.click(BasePageLocators.BUTTON_CLOSE)
        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)

        #Переход на страницу заказов и проверка что счетчик увеличился
        basepage.click(BasePageLocators.BUTTON_LIST_ORDER)
        basepage.wait_presence_of_element_located(OrderListPageLocators.COUNT_ALL_ORDERS)
        count_all_orders_end = basepage.get_answer(OrderListPageLocators.COUNT_ALL_ORDERS)
        count_all_orders_end = int(count_all_orders_end)
        count_all_orders = int(count_all_orders)
        assert (count_all_orders_end - count_all_orders) == 1




    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_order_today_count_plus(self, data_new3, driver_double):
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
        basepage.wait_presence_of_element_located(LoginPageLocator.BUTTON_RESET_PASSWORD)
        login.click_button_enter()

        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)
        basepage.click(BasePageLocators.BUTTON_LIST_ORDER)
        basepage.wait_presence_of_element_located(OrderListPageLocators.COUNT_ALL_ORDERS)




        order_today = basepage.get_answer(OrderListPageLocators.COUNT_ORDERS_TODAY)
        #тут перешел на страницу конструктора

        # тут перешел на страницу конструктора
        basepage.click(BasePageLocators.BUTTON_CONSTRUCTOR)
        # time.sleep(1)
        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)

        basepage.drop_ingredient_korzina()
        basepage.click(BasePageLocators.BUTTON_CREATE_ORDER)

        basepage.wait_active_element(BasePageLocators.BUTTON_CLOSE)
        basepage.wait_title_change_not_9999()
        count_order = basepage.get_answer(BasePageLocators.ID_ORDER)
        assert count_order != "9999"
        basepage.click(BasePageLocators.BUTTON_CLOSE)
        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)

        # Переход на страницу заказов и проверка что счетчик увеличился
        basepage.click(BasePageLocators.BUTTON_LIST_ORDER)

        # time.sleep(3)

        basepage.wait_title_change_not_x(order_today)
        # time.sleep(3)
        basepage.wait_presence_of_element_located(OrderListPageLocators.COUNT_ORDERS_TODAY)
        order_today_end = basepage.get_answer(OrderListPageLocators.COUNT_ORDERS_TODAY)
        # time.sleep(3)

        order_today = int(order_today)
        order_today_end = int(order_today_end)
        assert order_today_end - order_today >= 1


    @allure.title("после оформления заказа его номер появляется в разделе В работе.")
    def test_order_frame_in_work(self, data_new3, driver_double):
        #Тут авторизация пользователя
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
        basepage.wait_presence_of_element_located(LoginPageLocator.BUTTON_RESET_PASSWORD)
        login.click_button_enter()

        basepage.drop_ingredient_korzina()
        basepage.click(BasePageLocators.BUTTON_CREATE_ORDER)

        basepage.wait_active_element(BasePageLocators.BUTTON_CLOSE)
        basepage.wait_title_change_not_9999()
        count_order = basepage.get_answer(BasePageLocators.ID_ORDER)
        count_order = "0" + count_order
        assert count_order != "9999"
        basepage.click(BasePageLocators.BUTTON_CLOSE)
        basepage.wait_active_element(BasePageLocators.BUTTON_CREATE_ORDER)

        # Переход на страницу заказов и проверка что счетчик увеличился
        basepage.click(BasePageLocators.BUTTON_LIST_ORDER)
        basepage.wait_title_change_not_xx(count_order)
        order_in_work = basepage.get_answer(OrderListPageLocators.ORDER_IN_WORK)
        assert count_order == order_in_work