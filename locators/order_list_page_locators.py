from selenium.webdriver.common.by import By


class OrderListPageLocators:
    FIRST_ORDER = (By.XPATH, '*//ul/li[1]/a[@class = "OrderHistory_link__1iNby"]')  # Первый заказ
    TITLE_SOSTAV = (By.XPATH, '*//div/p[3][@class = "text text_type_main-medium mb-8"]')  # Заголовок "Состав"
    LAST_ORDER_ACCOUNT = (By.XPATH, '*//ul/li//p[@class = "text text_type_digits-default"]')  # Последний заказ в
    # личном кабинете
    COUNT_ALL_ORDERS = (By.XPATH, '//div/p[contains(text(), "Выполнено за все время")]/following-sibling::p')  # Счетчик всех заказов
    COUNT_ORDERS_TODAY = (
    By.XPATH, '*//div/p[contains(text(), "Выполнено за сегодня")]/following-sibling::p')  # Счетчик заказов за день
    ORDER_IN_WORK = (
    By.XPATH, '//*[contains(@class, "OrderFeed_orderStatusBox")]//ul[2]/li')  # Счетчик заказов в работе