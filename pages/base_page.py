from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import data


class BasePage:
    #Локаторы для кейсов по восстановлению паролей

    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BUTTON_RESET_PASSWORD = (By.XPATH, "//*[contains(@href,'/forgot-password')]")
    EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")
    EYES_AREA = (By.XPATH, "//div[@class='input__icon input__icon-action']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")
    def open_base_page(self):
        self.driver.get(data.Urls.HOME_PAGE)

    @allure.step("Нажать на кнопку 'Войти в аккаунт'")
    def click_button_login_account(self):
        button = self.driver.find_element(*BasePage.BUTTON_ENTER_ACCOUNT)
        button.click()

    @allure.step("Нажать на cсылку 'Восстановить пароль'")
    def click_button_reset_password(self):
        button = self.driver.find_element(*BasePage.BUTTON_RESET_PASSWORD)
        button.click()

    @allure.step("Ввести Email")
    def enter_email_field(self):
        field = self.driver.find_element(*BasePage.EMAIL_FIELD)
        field.send_keys(data.FakeData.fake_email)

    @allure.step("Нажать на кнопку 'Восстановить'")
    def click_enter_button_restore(self):
        button = self.driver.find_element(*BasePage.RESTORE_BUTTON)
        button.click()

    @allure.step("Нажать на поле 'Пароль'")
    def click_frame_password(self):
        frame = self.driver.find_element(*BasePage.BUTTON_RESET_PASSWORD)
        frame.click()
    @allure.step("Нажать на кнопку 'показать/скрыть пароль'")
    def click_frame_password(self):
        frame = self.driver.find_element(*BasePage.EYES_AREA)
        frame.click()

    @allure.step('Получить текущий адрес страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание смены страницы')
    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(url))

    @allure.step('Ожидание появления элемента по локатору')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    @allure.step('Ожидание смены веб-странички с восстановлением пароля')
    def wait_for_url_changes_restore(self):
        self.wait_url_changes(data.Urls.HOME_PAGE + data.Urls.FORGOT_PASSWORD_END_POINT)


    @allure.step('Получение и возврат атрибута вида "тип" со значением "текст"')
    def get_input_status(self):
        input_status = self.wait_and_find_element(self.PASSWORD_FIELD)
        return input_status.get_attribute("type") == 'text'