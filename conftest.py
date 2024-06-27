import pytest
from selenium import webdriver
import allure
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

        # options.maximize_window()
        # options.add_argument('--window-size=2560,1440')
        driver = webdriver.Firefox(options=options)
    driver.get(Urls.HOME_PAGE)#Тут пишем базовую страницу
    driver.maximize_window()

    yield driver
    driver.quit()