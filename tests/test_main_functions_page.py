import allure
from data import Urls
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from pages.loginPage import LoginPage


class TestMainPage:
    @allure.title("переход по клику на «Конструктор»")
    def test_go_to_page_constructor(self, driver_double):
        basepage = BasePage(driver_double)
        basepage.click_construcktor()
        assert basepage.get_current_url() == Urls.HOME_PAGE + "/"

    @allure.title("переход по клику на «Лента заказов»")
    def test_go_to_page_list_orders(self, driver_double):
        basepage = BasePage(driver_double)
        basepage.click_order_list()
        assert basepage.get_current_url() == Urls.HOME_PAGE + Urls.LIST_OF_ORDERS_END_POINT

    @allure.title("если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_ingredient(self, driver_double):
        basepage = BasePage(driver_double)
        basepage.click_bulka_wait_id_ingredient()
        assert basepage.get_title_ingredient() == "Детали ингредиента"

    @allure.title("всплывающее окно закрывается кликом по крестику")
    def test_close_popup_ingredient(self, driver_double):
        basepage = BasePage(driver_double)
        basepage.get_id_ingredient_close_window
        assert basepage.wait_presence_of_element_located(BasePageLocators.BUTTON_ENTER_ACCOUNT)

    #
    @allure.title("при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается,")
    def test_add_ingredient_in_order_counter(self, driver_double):
        basepage = BasePage(driver_double)
        count_ingredient = basepage.get_count_ingredient()
        assert count_ingredient == "0"
        basepage.drop_ingredient_korzina()
        count_ingredient = basepage.get_count_ingredient()
        assert count_ingredient == "2"

    @allure.title("залогиненный пользователь может оформить заказ.")
    def test_create_order_auth_user(self, create_user_data, driver_double):
        basepage = BasePage(driver_double)
        basepage.click_button_login_account()
        login = LoginPage(driver_double)
        login.enter_login_password(create_user_data)
        basepage.create_order_get_id()
        assert basepage.create_order_get_id() != "0"
