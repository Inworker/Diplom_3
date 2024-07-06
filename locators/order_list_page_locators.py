from selenium.webdriver.common.by import By


class OrderListPageLocators:
    FIRST_ORDER = (By.XPATH, '*//ul/li[1]/a[@class = "OrderHistory_link__1iNby"]')  # Первый заказ
    TITLE_SOSTAV = (By.XPATH, '*//div/p[3][@class = "text text_type_main-medium mb-8"]')  # Заголовок "Состав"
    LAST_ORDER_ACCOUNT = (By.XPATH, '*//ul/li//p[@class = "text text_type_digits-default"]')  # Последний заказ в
    # личном кабинете
    COUNT_ALL_ORDERS = (By.XPATH, '*//div[@class = "undefined mb-15"]/p[2]')  # Счетчик всех заказов
    COUNT_ORDERS_TODAY = (
    By.XPATH, '*//div[@class = "OrderFeed_ordersData__1L6Iv"]/div[3]/p[2]')  # Счетчик заказов за день
    ORDER_IN_WORK = (
    By.XPATH, '*//div[@class = "OrderFeed_orderStatusBox__1d4q2 mb-15"]/ul[2]/li')  # Счетчик заказов в работе
