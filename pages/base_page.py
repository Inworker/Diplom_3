from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
from seletools.actions import drag_and_drop

from locators.base_page_locators import BasePageLocators
from locators.order_list_page_locators import OrderListPageLocators


class BasePage:
    # Локаторы для кейсов по восстановлению паролей
    # Главная страцница



    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")  # Главная страница
    def open_base_page(self):
        self.driver.get(data.Urls.HOME_PAGE)

    @allure.step("Нажать на кнопку 'Войти в аккаунт'")  # Главная страница
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



    # BUTTON_ACCOUNT = (By.XPATH, "//a[contains(@href,'/account') or text()='Личный Кабинет']")

    # Локаторы по логину в Личный кабинет
    # BUTTON_ACCOUNT = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]")



    @allure.step('Получить текст ответа')
    def get_answer(self, locator_a):
        answer = self.driver.find_element(*locator_a)
        return answer.text

    #Методы по логину в личный кабинет
    # @allure.step('Регистрация пользователя')
    # def get_data_for_login(self, data_new3):
    #     payload = data_new3
    #     return payload

    def get_order_list(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(BasePage.BUTTON_ORDER_HISTORY))
        return self.driver.find_element(*BasePage.BUTTON_ORDER_HISTORY)
    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_button_account(self):
        button = self.driver.find_element(*BasePageLocators.BUTTON_ACCOUNT)
        button.click()


    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        button = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", button)

    def wait_button_save(self):
        self.wait_and_find_element(BasePage.BUTTON_SAVE)

    def wait_button_login(self):
        self.wait_element_clickable(self.BUTTON_ACCOUNT)









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
        WebDriverWait(self.driver, 30).until_not(expected_conditions.text_to_be_present_in_element(BasePageLocators.ID_ORDER, '9999'))
        self.driver.find_element(*BasePageLocators.ID_ORDER)

    @allure.step("Подождать пока список заказов будет != ")
    def wait_title_change_not_x(self, order):
        WebDriverWait(self.driver, 30).until_not(expected_conditions.text_to_be_present_in_element(BasePageLocators.ID_ORDER, order))
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

    @allure.step("Подождать пока  будет != чему то")
    def wait_title_change_not_xx(self, order):
        WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element(OrderListPageLocators.ORDER_IN_WORK, order))
        self.driver.find_element(*OrderListPageLocators.ORDER_IN_WORK)









