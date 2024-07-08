import allure

from locators.account_page_locators import AccountPageLocators
from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step("Ожидание кнопки Сохранить")
    def wait_button_save(self):
        self.wait_and_find_element(AccountPageLocators.BUTTON_SAVE)

    @allure.step("Клик на кнопку История")
    def click_history(self):
        self.click(AccountPageLocators.BUTTON_HISTORY_PROFILE)

    @allure.step("Подождать кнопку Сохранить и нажать на История")
    def wait_button_save_click_history(self):
        self.wait_button_save()
        self.click_history()

    @allure.step("Получить текст кнопки Сохранить")
    def get_text_button_save(self):
        text = self.get_answer(AccountPageLocators.BUTTON_SAVE)
        return text

    @allure.step("Подождать кнопку Сохранить и нажать выход")
    def wait_button_save_click_exit(self):
        self.wait_button_save()
        self.click_exit()

    @allure.step("Нажать кнопку выход")
    def click_exit(self):
        self.click(AccountPageLocators.BUTTON_EXIT)

    @allure.step("Подождать последний созданный заказ в аккаунте")
    def wait_last_order_account(self):
        self.wait_presence_of_element_located(OrderListPageLocators.LAST_ORDER_ACCOUNT)

    @allure.step("Получить номер заказа в аккаунте")
    def get_count_order_account(self):
        text = self.get_answer(OrderListPageLocators.LAST_ORDER_ACCOUNT)
        return text

    @allure.step("Подождать кнопку Сохранить и нажать на кнопку История ")
    def wait_button_save_click_history_wait_order(self):
        self.wait_button_save_click_history()
        self.wait_last_order_account()
