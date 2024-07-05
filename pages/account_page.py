from locators.account_page_locators import AccountPageLocators
from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    def wait_button_save(self):
        self.wait_and_find_element(AccountPageLocators.BUTTON_SAVE)
    def click_history(self):
        self.click(AccountPageLocators.BUTTON_HISTORY_PROFILE)


    def wait_button_save_click_history(self):
        self.wait_button_save()
        self.click_history()

    def get_text_button_save(self):
        text = self.get_answer(AccountPageLocators.BUTTON_SAVE)
        return text

    def wait_button_save_click_exit(self):
        self.wait_button_save()
        self.click_exit()

    def click_exit(self):
        self.click(AccountPageLocators.BUTTON_EXIT)

    def wait_last_order_account(self):
        self.wait_presence_of_element_located(OrderListPageLocators.LAST_ORDER_ACCOUNT)

    def get_count_order_account(self):
        text = self.get_answer(OrderListPageLocators.LAST_ORDER_ACCOUNT)
        return text

    def wait_button_save_click_history_wait_order(self):
        self.wait_button_save_click_history()
        self.wait_last_order_account()