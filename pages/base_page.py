from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
from seletools.actions import drag_and_drop


class BasePage:
    # Локаторы для кейсов по восстановлению паролей
    # Главная страцница
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Страница логина
    BUTTON_RESET_PASSWORD = (By.XPATH, "//*[contains(@href,'/forgot-password')]")
    # Cтраница сброса пароля
    EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")
    EYES_AREA = (By.XPATH, "//div[@class='input__icon input__icon-action']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")  # Главная страница
    def open_base_page(self):
        self.driver.get(data.Urls.HOME_PAGE)

    @allure.step("Нажать на кнопку 'Войти в аккаунт'")  # Главная страница
    def click_button_login_account(self):
        button = self.driver.find_element(*BasePage.BUTTON_ENTER_ACCOUNT)
        button.click()

    @allure.step("Нажать на cсылку 'Восстановить пароль'")  # Страцница логина
    def click_button_reset_password(self):
        button = self.driver.find_element(*BasePage.BUTTON_RESET_PASSWORD)
        button.click()

    @allure.step("Ввести Email")  # Страцница сброса пароля
    def enter_email_field(self):
        field = self.driver.find_element(*BasePage.EMAIL_FIELD)
        field.send_keys(data.FakeData.fake_email)

    @allure.step("Нажать на кнопку 'Восстановить'")  # Страцница сброса пароля
    def click_enter_button_restore(self):
        button = self.driver.find_element(*BasePage.RESTORE_BUTTON)
        button.click()

    @allure.step("Нажать на поле 'Пароль'")  # Страцница сброса пароля
    def click_frame_password(self):
        frame = self.driver.find_element(*BasePage.BUTTON_RESET_PASSWORD)
        frame.click()

    @allure.step("Нажать на кнопку 'показать/скрыть пароль'")  # Страцница сброса пароля
    def click_frame_password(self):
        frame = self.driver.find_element(*BasePage.EYES_AREA)
        frame.click()

    @allure.step('Получить текущий адрес страницы')  # общий метод
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание смены страницы')  # общий метод
    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 30).until(expected_conditions.url_changes(url))

    @allure.step('Ожидание смены веб-странички с восстановлением пароля')  # Страцница сброса пароля
    def wait_for_url_changes_restore(self):
        self.wait_url_changes(data.Urls.HOME_PAGE + data.Urls.FORGOT_PASSWORD_END_POINT)

    @allure.step('Получение и возврат атрибута вида "тип" со значением "текст"')  # Страцница сброса пароля
    def get_input_status(self):
        input_status = self.wait_and_find_element(self.PASSWORD_FIELD)
        return input_status.get_attribute("type") == 'text'

    # BUTTON_ACCOUNT = (By.XPATH, "//a[contains(@href,'/account') or text()='Личный Кабинет']")

    # Локаторы по логину в Личный кабинет
    # BUTTON_ACCOUNT = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]")
    BUTTON_ACCOUNT = (By.XPATH, "//*[contains(@href,'/account')]")
    BUTTON_HISTORY_PROFILE = (By.XPATH, "//a[text()='История заказов']")
    # BUTTON_SAVE = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']")
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input")
    INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']")
    BUTTON_ORDER_HISTORY = (By.XPATH, "//*[contains(@href,'/account/order-history')]")
    LIST_ORDERS = (By.XPATH, '//ul[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]')



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
        button = self.driver.find_element(*BasePage.BUTTON_ACCOUNT)
        button.click()


    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        button = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", button)

    def wait_button_save(self):
        self.wait_and_find_element(BasePage.BUTTON_SAVE)

    def wait_button_login(self):
        self.wait_element_clickable(self.BUTTON_ACCOUNT)

    @allure.step('Заполнить поле "Email"')
    def enter_field_Email(self, email):
        field = self.driver.find_element(*BasePage.EMAIL_FIELD)
        field.send_keys(email)



    @allure.step('Заполнить поле "Пароль"')
    def enter_field_password(self, password):
        field = self.driver.find_element(*BasePage.INPUT_PASSWORD)
        field.send_keys(password)


    @allure.step('Нажать на кнопку "Войти"')
    def click_button_enter(self):
        button = self.driver.find_element(*BasePage.BUTTON_ENTER)
        button.click()

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

    # @allure.step("Нажать на кнопку Закрыть всплывающего окна")
    # def click_button_close(self):
    #     buttons = self.driver.find_elements(*BasePage.BUTTON_CLOSE)
    #     first_button = buttons[0]
    #     first_button.click()

    @allure.step("Перетащить ингредиент в корзину")
    def drop_ingredient_korzina(self):
        ingredient = self.wait_presence_of_element_located(BasePage.FIRST_INGREDIENT_BULKA)
        korzina = self.wait_presence_of_element_located(BasePage.KORZINA)
        drag_and_drop(self.driver, ingredient, korzina)


    #   Локаторы для страницы основных функций
    BUTTON_CONSTRUCTOR =(By.XPATH, "//a/p[text()='Конструктор']")
    BUTTON_LIST_ORDER = (By.XPATH, "//a/p[text()='Лента Заказов']")
    FIRST_INGREDIENT_BULKA = (By.XPATH, "*//ul[1]/a[1]")
    TITLE_DETAILS_INGREDIENT = (By.XPATH, "//*//h2[text()='Детали ингредиента']")
    BUTTON_CLOSE = (By.XPATH, "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    KORZINA = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    COUNT_INGREDIENT = (By.XPATH, "*//ul[1]//p[@class = 'counter_counter__num__3nue1']")
    BUTTON_CREATE_ORDER = (By.XPATH, '*//button[text() = "Оформить заказ"]')
    TITLE_ORDER_IN_PROCESS = (By.XPATH, '*//p[text() = "Ваш заказ начали готовить"]')
    ID_ORDER = (By.XPATH, '*//h2[@class = "Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    FIRST_ORDER = (By.XPATH, '*//ul/li[1]/a[@class = "OrderHistory_link__1iNby"]')
    LAST_ORDER_LENTA = (By.XPATH, "//ul//a//p[@class = 'text text_type_digits-default']")


    #Локаторы для страницы ленты заказов

    TITLE_SOSTAV = (By.XPATH, '*//div/p[3][@class = "text text_type_main-medium mb-8"]')
    LAST_ORDER_ACCOUNT = (By.XPATH, '*//ul/li//p[@class = "text text_type_digits-default"]')
    COUNT_ALL_ORDERS = (By.XPATH, '*//div[@class = "undefined mb-15"]/p[2]')
    COUNT_ORDERS_TODAY = (By.XPATH, '*//div[@class = "OrderFeed_ordersData__1L6Iv"]/div[3]/p[2]')
    ORDER_IN_WORK = (By.XPATH, '*//div[@class = "OrderFeed_orderStatusBox__1d4q2 mb-15"]/ul[2]/li')
    @allure.step("Подождать пока список заказов будет != 9999")
    def wait_title_change_not_9999(self):
        WebDriverWait(self.driver, 30).until_not(expected_conditions.text_to_be_present_in_element(self.ID_ORDER, '9999'))
        self.driver.find_element(*self.ID_ORDER)

    @allure.step("Подождать пока список заказов будет != 9999")
    def wait_title_change_not_x(self, order):
        WebDriverWait(self.driver, 30).until_not(expected_conditions.text_to_be_present_in_element(self.ID_ORDER, order))
        self.driver.find_element(*self.ID_ORDER)

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
    def wait_title_change_not_xx(self, locator, text):
        WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element(self.locator, text))
        self.driver.find_element(*self.locator)








