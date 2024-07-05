import allure
from locators.base_page_locators import BasePageLocators
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.loginPage import LoginPage
from pages.order_list_page import OrderListPage


class TestOrdersList:

    @allure.title("если кликнуть на заказ, откроется всплывающее окно с деталями,")
    def test_get_window_details(self, driver_double):
        basepage = BasePage(driver_double)
        basepage.get_window_sostav()
        sostav = basepage.get_title_sostav()
        assert sostav == "Cостав"

    @allure.title("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,")
    def test_get_order_user_page_order_history(self, data_new3, driver_double):
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        login = LoginPage(driver_double)
        login.enter_login_password(data_new3)
        basepage.create_order_wait_id_not_999()
        count_order = basepage.get_id_order()
        assert count_order != "9999"
        basepage.click_button_close_wait_active_create_order_account()
        account_page = AccountPage(driver_double)
        account_page.wait_button_save_click_history_wait_order()
        count_order_account = account_page.get_count_order_account()
        assert count_order in count_order_account
        basepage.click_order_list()
        order_list = OrderListPage(driver_double)
        order_list.wait_last_order_account()
        order_lenta = order_list.get_last_order_account()
        assert order_lenta == count_order_account

    @allure.title("при создании нового заказа счётчик Выполнено за всё время увеличивается,")
    def test_count_all_time(self, data_new3, driver_double):
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        login = LoginPage(driver_double)
        login.enter_login_password(data_new3)
        basepage.wait_create_order_active_click_order_list()
        order_page = OrderListPage(driver_double)
        order_page.wait_count_all_orders()
        count_all_orders = order_page.get_count_all_orders()
        basepage.click_construcktor()
        basepage.create_order_wait_id_not_999()
        count_order = basepage.get_id_order()
        assert count_order != "9999"
        basepage.click_button_close()
        basepage.wait_create_order_active()
        basepage.click_order_list()
        order_page.wait_count_all_orders()
        count_all_orders_end = order_page.get_count_all_orders()
        count_all_orders_end = int(count_all_orders_end)
        count_all_orders = int(count_all_orders)
        assert (count_all_orders_end - count_all_orders) == 1

    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_order_today_count_plus(self, data_new3, driver_double):
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        login = LoginPage(driver_double)
        login.enter_login_password(data_new3)
        basepage.wait_create_order_active()
        basepage.click_order_list()
        order_page = OrderListPage(driver_double)
        order_page.wait_count_all_orders()
        order_today = order_page.get_count_orders_today()
        basepage.click_construcktor()
        basepage.create_order_wait_id_not_999()
        count_order = basepage.get_answer(BasePageLocators.ID_ORDER)
        assert count_order != "9999"
        basepage.check_count_plus(order_today)
        order_page.wait_count_orders_today()
        order_today_end = order_page.get_count_orders_today()
        order_today = int(order_today)
        order_today_end = int(order_today_end)
        assert order_today_end - order_today >= 1

    @allure.title("после оформления заказа его номер появляется в разделе В работе.")
    def test_order_frame_in_work(self, data_new3, driver_double):
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        login = LoginPage(driver_double)
        login.enter_login_password(data_new3)
        basepage.create_order_wait_id_not_999()
        count_order = basepage.get_id_order()
        count_order = "0" + count_order
        assert count_order != "9999"
        basepage.count_in_work(count_order)
        order_in_work = basepage.get_order_in_work()
        assert count_order == order_in_work
