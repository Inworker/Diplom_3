import time

import allure

from data import Urls
from pages.base_page import BasePage


class TestMainPage:
    @allure.title("переход по клику на «Конструктор»")
    def test_go_to_page_constructor(self, driver_double):
        login = BasePage(driver_double)
        login.click(BasePage.BUTTON_CONSTRUCTOR)
        assert login.get_current_url() == Urls.HOME_PAGE + "/"





    @allure.title("переход по клику на «Лента заказов»")
    def test_go_to_page_constructor(self, driver_double):
        login = BasePage(driver_double)
        login.click(BasePage.BUTTON_LIST_ORDER)
        assert login.get_current_url() == Urls.HOME_PAGE + Urls.LIST_OF_ORDERS_END_POINT

    @allure.title("если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_ingredient(self, driver_double):
        login = BasePage(driver_double)
        login.click(BasePage.FIRST_INGREDIENT_BULKA)
        # login.click(BasePage.TITLE_DETAILS_INGREDIENT)
        # login.wait_title("Детали ингредиента")
        # time.sleep(5)
        login.wait_presence_of_element_located(BasePage.TITLE_DETAILS_INGREDIENT)
        assert login.get_answer(BasePage.TITLE_DETAILS_INGREDIENT) == "Детали ингредиента"



    @allure.title("всплывающее окно закрывается кликом по крестику")
    def test_close_popup_ingredient(self, driver_double):
        login = BasePage(driver_double)
        login.click(BasePage.FIRST_INGREDIENT_BULKA)
        login.wait_presence_of_element_located(BasePage.TITLE_DETAILS_INGREDIENT)
        login.click(BasePage.BUTTON_CLOSE)
        assert login.wait_presence_of_element_located(BasePage.BUTTON_ENTER_ACCOUNT)
    #
    @allure.title("при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается,")
    def test_add_angreedient_in_order_counter(self, driver_double):
        login = BasePage(driver_double)
        count_ingredient =  login.get_answer(BasePage.COUNT_INGREDIENT)
        assert count_ingredient == "0"
        login.drop_ingredient_korzina()
        count_ingredient = login.get_answer(BasePage.COUNT_INGREDIENT)
        assert count_ingredient == "2"

    @allure.title("залогиненный пользователь может оформить заказ.")
    def test_create_order_auth_user(self, data_new3, driver_double):
        payload = data_new3
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        basepage.enter_field_Email(payload["email"])
        basepage.enter_field_password(payload["password"])
        basepage.click_button_enter()
        # time.sleep(1)  # тут пока не смог сделать ожидание
        basepage.drop_ingredient_korzina()
        # time.sleep(1)  # тут пока не смог сделать ожидание
        basepage.click(basepage.BUTTON_CREATE_ORDER)
        basepage.wait_presence_of_element_located(basepage.ID_ORDER)
        # basepage.wait_title("Ваш заказ начали готовить")
        count_order = basepage.get_answer(basepage.ID_ORDER)
        assert count_order != "0"

