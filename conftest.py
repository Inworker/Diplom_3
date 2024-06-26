import pytest
from selenium import webdriver
import allure

@allure.step('Запуск драйвера сразу для двух браузеров - "Firefox" и "Chrome"')
@pytest.fixture(params=['firefox', 'chrome'])
def driver_both(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    driver.get(URL.BASE_PAGE)#Тут пишем базовую страницу

    yield driver
    driver.quit()