from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):

    def wait_last_order_account(self):
        self.wait_presence_of_element_located(OrderListPageLocators.LAST_ORDER_ACCOUNT)

    def get_last_order_account(self):
        text = self.get_answer(OrderListPageLocators.LAST_ORDER_ACCOUNT)
        return text

    def wait_count_all_orders(self):
        self.wait_presence_of_element_located(OrderListPageLocators.COUNT_ALL_ORDERS)

    def get_count_all_orders(self):
        text = self.get_answer(OrderListPageLocators.COUNT_ALL_ORDERS)
        return text

    def get_count_orders_today(self):
        text = self.get_answer(OrderListPageLocators.COUNT_ORDERS_TODAY)
        return text

    def wait_count_orders_today(self):
        self.wait_presence_of_element_located(OrderListPageLocators.COUNT_ORDERS_TODAY)
