from selenium.webdriver.common.by import By

class OrderListPageLocators:
    FIRST_ORDER = (By.XPATH, '*//ul/li[1]/a[@class = "OrderHistory_link__1iNby"]')
    TITLE_SOSTAV = (By.XPATH, '*//div/p[3][@class = "text text_type_main-medium mb-8"]')
    # Локаторы для страницы ленты заказов

    LAST_ORDER_ACCOUNT = (By.XPATH, '*//ul/li//p[@class = "text text_type_digits-default"]')
    COUNT_ALL_ORDERS = (By.XPATH, '*//div[@class = "undefined mb-15"]/p[2]')
    COUNT_ORDERS_TODAY = (By.XPATH, '*//div[@class = "OrderFeed_ordersData__1L6Iv"]/div[3]/p[2]')
    ORDER_IN_WORK = (By.XPATH, '*//div[@class = "OrderFeed_orderStatusBox__1d4q2 mb-15"]/ul[2]/li')