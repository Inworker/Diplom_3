import time

import allure

from pages.base_page import BasePage


class TestOrdersList:

    @allure.title("если кликнуть на заказ, откроется всплывающее окно с деталями,")
    def test_get_window_details(self, driver_double):
        order_list = BasePage(driver_double)
        order_list.click(BasePage.BUTTON_LIST_ORDER)
        # time.sleep(1)
        order_list.wait_active_element(order_list.FIRST_ORDER)
        order_list.click(BasePage.FIRST_ORDER)
        # time.sleep(1)
        order_list.wait_presence_of_element_located(order_list.TITLE_SOSTAV)
        sostav = order_list.get_answer(order_list.TITLE_SOSTAV)
        assert sostav == "Cостав"


    @allure.title("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,")
    def test_get_order_user_page_order_history(self,data_new3, driver_double):
        payload = data_new3
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        basepage.enter_field_Email(payload["email"])
        basepage.enter_field_password(payload["password"])
        basepage.click_button_enter()
        basepage.drop_ingredient_korzina()
        basepage.click(basepage.BUTTON_CREATE_ORDER)
        # basepage.wait_presence_of_element_located(basepage.ID_ORDER)
        basepage.wait_title_change_not_9999()
        time.sleep(3)#Это надо обыграть как то
        # basepage.wait_presence_of_element_located(BasePage.TITLE_ORDER_IN_PROCESS)
        count_order = basepage.get_answer(basepage.ID_ORDER)
        assert count_order != "9999"
        basepage.click(BasePage.BUTTON_CLOSE)
        # basepage.wait_presence_of_element_located(BasePage.BUTTON_ENTER_ACCOUNT)
        time.sleep(3)
        basepage.click_button_account()
        basepage.wait_presence_of_element_located(BasePage.BUTTON_SAVE)
        basepage.click(basepage.BUTTON_HISTORY_PROFILE)
        time.sleep(1)
        count_order_account = basepage.get_answer(basepage.LAST_ORDER_ACCOUNT)
        assert  count_order in count_order_account
        basepage.click(BasePage.BUTTON_LIST_ORDER)
        time.sleep(3)
        order_lenta = basepage.get_answer(basepage.LAST_ORDER_ACCOUNT)
        # orders = basepage.get_list_orders
        # orders = orders.text
        # basepage.wait_presence_of_element_located(basepage.)
        assert order_lenta == count_order_account




    @allure.title("при создании нового заказа счётчик Выполнено за всё время увеличивается,")
    def test_count_all_time(self, data_new3, driver_double):
        #Тут авторизация пользователя
        payload = data_new3
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        basepage.enter_field_Email(payload["email"])
        basepage.enter_field_password(payload["password"])
        basepage.click_button_enter()
        #Тут перход на страницу Лента заказаов и получение счетчика "Выполнено за все время
        time.sleep(3)  # Это надо обыграть как то

        basepage.click(BasePage.BUTTON_LIST_ORDER)
        time.sleep(3)  # Это надо обыграть как то
        #Тут получил список заказов за все время
        count_all_orders = basepage.get_answer(basepage.COUNT_ALL_ORDERS)
        time.sleep(3)

        #тут перешел на страницу конструктора
        basepage.click(basepage.BUTTON_CONSTRUCTOR)
        time.sleep(1)
        #тут создание заказа
        basepage.drop_ingredient_korzina()
        basepage.click(basepage.BUTTON_CREATE_ORDER)
        # basepage.wait_presence_of_element_located(basepage.ID_ORDER)
        basepage.wait_title_change_not_9999()
        time.sleep(3)  # Это надо обыграть как то
        # basepage.wait_presence_of_element_located(BasePage.TITLE_ORDER_IN_PROCESS)
        #тут получил номер нового заказа
        count_order = basepage.get_answer(basepage.ID_ORDER)
        time.sleep(3)
        assert count_order != "9999"
        basepage.click(BasePage.BUTTON_CLOSE)
        time.sleep(3)
        #Переход на страницу заказов и проверка что счетчик увеличился
        basepage.click(BasePage.BUTTON_LIST_ORDER)
        time.sleep(3)
        count_all_orders_end = basepage.get_answer(basepage.COUNT_ALL_ORDERS)
        count_all_orders_end = int(count_all_orders_end)
        count_all_orders = int(count_all_orders)
        assert (count_all_orders_end - count_all_orders) == 1




    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_order_today_count_plus(self, data_new3, driver_double):
        payload = data_new3
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        basepage.enter_field_Email(payload["email"])
        basepage.enter_field_password(payload["password"])
        basepage.click_button_enter()
        # Тут перход на страницу Лента заказаов и получение счетчика "Выполнено за сегодня
        time.sleep(3)  # Это надо обыграть как то
        basepage.click(BasePage.BUTTON_LIST_ORDER)
        time.sleep(3)  # Это надо обыграть как то

        order_today = basepage.get_answer(basepage.COUNT_ORDERS_TODAY)
        #тут перешел на страницу конструктора
        basepage.click(basepage.BUTTON_CONSTRUCTOR)
        time.sleep(1)
        #тут создание заказа
        basepage.drop_ingredient_korzina()
        basepage.click(basepage.BUTTON_CREATE_ORDER)
        # basepage.wait_presence_of_element_located(basepage.ID_ORDER)
        basepage.wait_title_change_not_9999()
        time.sleep(3)  # Это надо обыграть как то
        # basepage.wait_presence_of_element_located(BasePage.TITLE_ORDER_IN_PROCESS)
        #тут получил номер нового заказа
        count_order = basepage.get_answer(basepage.ID_ORDER)
        time.sleep(3)
        assert count_order != "9999"
        basepage.click(BasePage.BUTTON_CLOSE)
        time.sleep(3)
        #Переход на страницу заказов и проверка что счетчик увеличился
        basepage.click(BasePage.BUTTON_LIST_ORDER)
        time.sleep(3)

        basepage.wait_title_change_not_x(order_today)
        time.sleep(3)

        order_today_end = basepage.get_answer(basepage.COUNT_ORDERS_TODAY)
        time.sleep(3)

        order_today = int(order_today)
        order_today_end = int(order_today_end)
        assert order_today_end - order_today >= 1


    @allure.title("после оформления заказа его номер появляется в разделе В работе.")
    def test_order_frame_in_work(self, data_new3, driver_double):
        #Тут авторизация пользователя
        payload = data_new3
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        basepage.enter_field_Email(payload["email"])
        basepage.enter_field_password(payload["password"])
        basepage.click_button_enter()
        time.sleep(3)
        # тут создание заказа
        basepage.drop_ingredient_korzina()
        basepage.click(basepage.BUTTON_CREATE_ORDER)
        # basepage.wait_presence_of_element_located(basepage.ID_ORDER)
        basepage.wait_title_change_not_9999()
        time.sleep(3)  # Это надо обыграть как то
        # basepage.wait_presence_of_element_located(BasePage.TITLE_ORDER_IN_PROCESS)
        # тут получил номер нового заказа
        count_order = basepage.get_answer(basepage.ID_ORDER)
        count_order =  "0" + count_order
        time.sleep(3)
        assert count_order != "9999"
        basepage.click(BasePage.BUTTON_CLOSE)
        time.sleep(3)
        # Переход на страницу заказов и проверка что счетчик увеличился
        basepage.click(BasePage.BUTTON_LIST_ORDER)
        # time.sleep(3)
        # basepage.wait_title_change_not_xx(basepage.ORDER_IN_WORK, count_order)
        order_in_work = basepage.get_answer(basepage.ORDER_IN_WORK)
        assert count_order == order_in_work