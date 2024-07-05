import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
from seletools.actions import drag_and_drop
from locators.base_page_locators import BasePageLocators
from locators.order_list_page_locators import OrderListPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")
    def open_base_page(self):
        self.driver.get(data.Urls.HOME_PAGE)

    @allure.step("Нажать на кнопку 'Войти в аккаунт'")
    def click_button_login_account(self):
        button = self.driver.find_element(*BasePageLocators.BUTTON_ENTER_ACCOUNT)
        button.click()

    @allure.step('Получить текущий адрес страницы')  # общий метод
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание смены страницы')  # общий метод
    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 30).until(expected_conditions.url_changes(url))

    @allure.step('Ожидание смены веб-странички с восстановлением пароля')  # Страцница сброса пароля
    def wait_for_url_changes_restore(self):
        self.wait_url_changes(data.Urls.HOME_PAGE + data.Urls.FORGOT_PASSWORD_END_POINT)

    def click_construcktor(self):
        self.click(BasePageLocators.BUTTON_CONSTRUCTOR)

    def click_order_list(self):
        self.click(BasePageLocators.BUTTON_LIST_ORDER)

    def wait_active_first_order(self):
        self.wait_active_element(OrderListPageLocators.FIRST_ORDER)

    def click_first_order(self):
        self.click(OrderListPageLocators.FIRST_ORDER)

    def wait_title_sostav(self):
        self.wait_presence_of_element_located(OrderListPageLocators.TITLE_SOSTAV)

    @allure.step('Получить текст ответа')
    def get_answer(self, locator_a):
        answer = self.driver.find_element(*locator_a)
        return answer.text

    def get_order_list(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(BasePage.BUTTON_ORDER_HISTORY))
        return self.driver.find_element(*BasePage.BUTTON_ORDER_HISTORY)

    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_button_account(self):
        self.click(BasePageLocators.BUTTON_ACCOUNT)

    def click_first_bulka(self):
        self.click(BasePageLocators.FIRST_INGREDIENT_BULKA)

    def wait_id_ingredient(self):
        self.wait_presence_of_element_located(BasePageLocators.TITLE_DETAILS_INGREDIENT)

    def get_title_ingredient(self):
        text = self.get_answer(BasePageLocators.TITLE_DETAILS_INGREDIENT)
        return text

    def click_bulka_wait_id_ingredient(self):
        self.click_first_bulka()
        self.wait_id_ingredient()

    def get_id_ingredient_close_window(self):
        self.click_bulka_wait_id_ingredient()
        self.click_button_close()

    def click_button_close(self):
        self.click(BasePageLocators.BUTTON_CLOSE)

    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        button = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", button)

    def wait_button_login(self):
        self.wait_element_clickable(self.BUTTON_ACCOUNT)

    def get_count_ingredient(self):
        count = self.get_answer(BasePageLocators.COUNT_INGREDIENT)
        return count

    def check_count_plus(self, order_today):
        self.click_button_close
        self.wait_create_order_active()
        self.click_order_list()
        self.wait_title_change_not_x(order_today)

    @allure.step('Ожидание отображения элемента')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание активность документа')
    def wait_active_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание активность документа')
    def wait_presence_of_element_located(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_create_order_active(self):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(BasePageLocators.BUTTON_CREATE_ORDER))
        return self.driver.find_element(*BasePageLocators.BUTTON_CREATE_ORDER)

    @allure.step("Ожидание заголовка")
    def wait_title(self, title):
        WebDriverWait(self.driver, 30).until(expected_conditions.title_is(title))
        self.driver.find_element(title)

    @allure.step("Перетащить ингредиент в корзину")
    def drop_ingredient_korzina(self):
        ingredient = self.wait_presence_of_element_located(BasePageLocators.FIRST_INGREDIENT_BULKA)
        korzina = self.wait_presence_of_element_located(BasePageLocators.KORZINA)
        drag_and_drop(self.driver, ingredient, korzina)

    @allure.step("Подождать пока список заказов будет != 9999")
    def wait_title_change_not_9999(self):
        WebDriverWait(self.driver, 30).until_not(
            expected_conditions.text_to_be_present_in_element(BasePageLocators.ID_ORDER, '9999'))
        self.driver.find_element(*BasePageLocators.ID_ORDER)

    @allure.step('Удалить # в начале заказа')
    def get_number_order_account(self):
        element = self.driver.find_element(BasePage.LAST_ORDER_ACCOUNT)
        text = element.text
        clean_text = text.replace("#", "")
        return str(clean_text)

    # @allure.step("Получить список заказов")
    # def get_list_orders(self):
    #     element =  self.driver.find_elements(*self.CREATED_ORDER_lenta)
    #     return element.text
    @allure.step("Подождать пока список заказов будет != ")
    def wait_title_change_not_x(self, order):
        WebDriverWait(self.driver, 30).until_not(
            expected_conditions.text_to_be_present_in_element(BasePageLocators.ID_ORDER, order))
        self.driver.find_element(*BasePageLocators.ID_ORDER)

    @allure.step("Подождать пока  будет != чему то")
    def wait_title_change_not_xx(self, order):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.text_to_be_present_in_element(OrderListPageLocators.ORDER_IN_WORK, order))
        self.driver.find_element(*OrderListPageLocators.ORDER_IN_WORK)

    def wait_active_create_order_click_acount(self):
        self.wait_create_order_active()
        self.click_button_account()

    def click_button_create_order(self):
        self.click(BasePageLocators.BUTTON_CREATE_ORDER)

    def wait_element_id_order(self):
        self.wait_presence_of_element_located(BasePageLocators.ID_ORDER)

    def get_id_order(self):
        text = self.get_answer(BasePageLocators.ID_ORDER)
        return text

    def get_title_sostav(self):
        sostav = self.get_answer(OrderListPageLocators.TITLE_SOSTAV)
        return sostav

    def create_order_get_id(self):
        self.wait_create_order_active()
        self.drop_ingredient_korzina()
        self.click_button_create_order()
        self.wait_element_id_order()
        count = self.get_id_order()
        return count

    def get_window_sostav(self):
        self.click_order_list()
        self.wait_active_first_order()
        self.click_first_order()
        self.wait_title_sostav()

    def wait_active_button_close(self):
        self.wait_active_element(BasePageLocators.BUTTON_CLOSE)

    def create_order_wait_id_not_999(self):
        self.wait_create_order_active()
        self.drop_ingredient_korzina()
        self.click_button_create_order()
        self.wait_active_button_close()
        self.wait_title_change_not_9999()

    def get_order_in_work(self):
        text = self.get_answer(OrderListPageLocators.ORDER_IN_WORK)
        return text

    def count_in_work(self, count_order):
        self.click_button_close()
        self.wait_create_order_active()
        self.click_order_list()
        self.wait_title_change_not_xx(count_order)

    def click_button_close_wait_active_create_order_account(self):
        self.click_button_close()
        self.wait_active_create_order_click_acount()

    def wait_create_order_active_click_order_list(self):
        self.wait_create_order_active()
        self.click_order_list()
