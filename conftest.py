import pytest
from selenium import webdriver
import allure
import helper
from data import Urls
import requests


@allure.step('Запуск драйвера сразу для двух браузеров - "Firefox" и "Chrome"')
@pytest.fixture(params=['firefox', 'chrome'])
def driver_double(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    driver.get(Urls.HOME_PAGE)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def create_user_data():
    payload = helper.CreateCurrierData().generate_courier_data()
    response_create_user = requests.post(Urls.HOME_PAGE + Urls.AUTH_REGISTER_USER_URL, data=payload)
    yield payload
    token = response_create_user.json()["accessToken"]
    requests.delete(Urls.HOME_PAGE + Urls.AUTH_USER_URL, data=payload, headers={"Authorization": token})
