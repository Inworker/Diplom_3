import allure
from data import Urls
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocator
from pages.base_page import BasePage
from pages.loginPage import LoginPage


class TestMainPage:
    @allure.title("переход по клику на «Конструктор»")
    def test_go_to_page_constructor(self, driver_double):
        basepage = BasePage(driver_double)
        basepage.click(BasePageLocators.BUTTON_CONSTRUCTOR)
        assert basepage.get_current_url() == Urls.HOME_PAGE + "/"


    @allure.title("переход по клику на «Лента заказов»")
    def test_go_to_page_list_orders(self, driver_double):
        basepage = BasePage(driver_double)
        basepage.click(BasePageLocators.BUTTON_LIST_ORDER)
        assert basepage.get_current_url() == Urls.HOME_PAGE + Urls.LIST_OF_ORDERS_END_POINT

    @allure.title("если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_ingredient(self, driver_double):
        basepage = BasePage(driver_double)
        basepage.click(BasePageLocators.FIRST_INGREDIENT_BULKA)
        basepage.wait_presence_of_element_located(BasePageLocators.TITLE_DETAILS_INGREDIENT)
        assert basepage.get_answer(BasePageLocators.TITLE_DETAILS_INGREDIENT) == "Детали ингредиента"



    @allure.title("всплывающее окно закрывается кликом по крестику")
    def test_close_popup_ingredient(self, driver_double):
        basepage = BasePage(driver_double)
        basepage.click(BasePageLocators.FIRST_INGREDIENT_BULKA)
        basepage.wait_presence_of_element_located(BasePageLocators.TITLE_DETAILS_INGREDIENT)
        basepage.click(BasePageLocators.BUTTON_CLOSE)
        assert basepage.wait_presence_of_element_located(BasePageLocators.BUTTON_ENTER_ACCOUNT)
    #
    @allure.title("при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается,")
    def test_add_angreedient_in_order_counter(self, driver_double):
        basepage = BasePage(driver_double)
        count_ingredient =  basepage.get_answer(BasePageLocators.COUNT_INGREDIENT)
        assert count_ingredient == "0"
        basepage.drop_ingredient_korzina()
        count_ingredient = basepage.get_answer(BasePageLocators.COUNT_INGREDIENT)
        assert count_ingredient == "2"

    @allure.title("залогиненный пользователь может оформить заказ.")
    def test_create_order_auth_user(self, data_new3, driver_double):
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
        # time.sleep(1)  # тут пока не смог сделать ожидание
        basepage.click(BasePageLocators.BUTTON_CREATE_ORDER)
        basepage.wait_presence_of_element_located(BasePageLocators.ID_ORDER)
        # basepage.wait_title("Ваш заказ начали готовить")
        count_order = basepage.get_answer(BasePageLocators.ID_ORDER)
        assert count_order != "0"





        ////////
        # Тут авторизация пользователя
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
        # Тут получил список заказов за все время
        count_all_orders = basepage.get_answer(OrderListPageLocators.COUNT_ALL_ORDERS)
        # time.sleep(3)

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
        basepage.wait_presence_of_element_located(OrderListPageLocators.COUNT_ALL_ORDERS)
        count_all_orders_end = basepage.get_answer(OrderListPageLocators.COUNT_ALL_ORDERS)
        count_all_orders_end = int(count_all_orders_end)
        count_all_orders = int(count_all_orders)
        assert (count_all_orders_end - count_all_orders) == 1

