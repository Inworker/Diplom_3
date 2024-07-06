from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage
import allure


class OrderListPage(BasePage):

    @allure.step("Ожиднание последнего заказа")
    def wait_last_order_account(self):
        self.wait_presence_of_element_located(OrderListPageLocators.LAST_ORDER_ACCOUNT)

    @allure.step("Получить последний заказа в аккаунте")
    def get_last_order_account(self):
        text = self.get_answer(OrderListPageLocators.LAST_ORDER_ACCOUNT)
        return text

    @allure.step("Ожидание счетчика всех заказов")
    def wait_count_all_orders(self):
        self.wait_presence_of_element_located(OrderListPageLocators.COUNT_ALL_ORDERS)

    @allure.step("Получить кол-во всех заказов")
    def get_count_all_orders(self):
        text = self.get_answer(OrderListPageLocators.COUNT_ALL_ORDERS)
        return text

    @allure.step("Поулчить кол-во заказов за текущий день")
    def get_count_orders_today(self):
        text = self.get_answer(OrderListPageLocators.COUNT_ORDERS_TODAY)
        return text

    @allure.step("Ожидание кол-ва заказов за день")
    def wait_count_orders_today(self):
        self.wait_presence_of_element_located(OrderListPageLocators.COUNT_ORDERS_TODAY)
