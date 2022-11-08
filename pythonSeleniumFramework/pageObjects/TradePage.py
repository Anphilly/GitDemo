from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TradePage:

    def __init__(self, driver):
        self.driver = driver
    search_box = (By.XPATH, "//input[@id='navigation-symbol-search']")
    symbol = (By.XPATH, "//li[@data-testid='symbol-search-dropdown:AAPL']")
    buy_button = (By.XPATH, "//button[@data-testid='TradeButton-buy']")
    quantity_input = (By.XPATH, "//input[@aria-label='Quantity Input']")
    order_type = (By.XPATH, "//button[@data-testid='order-type-dropdown-value']")
    market_order = (By.XPATH, "//li[@data-testid='order-type-dropdown:MARKET']")
    review_order = (By.ID, "review-order-button")
    send_order = (By.ID, "send-order-button")
    notification = (By.XPATH, "//div[text()='Notifications']")
    original_notification = (By.XPATH, "(//div[@class='NotificationCardstyled__NotificationCardWrapper-gqLrRi bFWws'])[1]")
    logout = (By.XPATH, "//div[text()='Log Out']")

    def get_search_box(self):
        return self.driver.find_element(*TradePage.search_box)

    def get_symbol(self):
        return self.driver.find_element(*TradePage.symbol)

    def get_buy_button(self):
        return self.driver.find_element(*TradePage.buy_button)

    def get_quantity_input(self):
        return self.driver.find_element(*TradePage.quantity_input)

    def get_order_type(self):
        return self.driver.find_element(*TradePage.order_type)

    def get_market_order(self):
        return self.driver.find_element(*TradePage.market_order)

    def get_review_order(self):
        return self.driver.find_element(*TradePage.review_order)

    def get_send_order(self):
        return self.driver.find_element(*TradePage.send_order)

    def get_notification(self):
        return self.driver.find_element(*TradePage.notification)

    def get_order_confirmation(self):
        original_confirmation = []
        original_message = [self.driver.find_element(*TradePage.original_notification).text]
        print(original_message)
        for records in original_message:
            original_confirmation.append(records)
        print(original_confirmation)
        assert original_message == original_confirmation
        return original_message

    def get_logout(self):
        return self.driver.find_element(*TradePage.logout)

# self.driver.find_element(By.XPATH, "//input[@id='navigation-symbol-search']").send_keys("AAPL")
# self.driver.find_element(By.XPATH, "//li[@data-testid='symbol-search-dropdown:AAPL']").click()
# self.driver.find_element(By.XPATH, "//button[@data-testid='TradeButton-buy']").click()
# self.driver.find_element(By.XPATH, "//input[@aria-label='Quantity Input']").send_keys(Keys.BACK_SPACE * 3)
# self.driver.find_element(By.XPATH, "//input[@data-testid='trade-quantity-input']").send_keys("2")
# self.driver.find_element(By.XPATH, "//button[@data-testid='order-type-dropdown-value']").click()
# self.driver.find_element(By.XPATH, "//li[@data-testid='order-type-dropdown:MARKET']").click()
# self.driver.find_element(By.ID, "review-order-button").click()
# self.driver.find_element(By.ID, "send-order-button").click()
# self.driver.find_element(By.ID, "review-order-button").click()
# self.driver.find_element(By.ID, "send-order-button").click()

        # original_confirmation = []
        # original_message = [self.driver.find_element(By.XPATH,
        #                                              "(//div[@class='NotificationCardstyled__NotificationCardWrapper-gqLrRi bFWws'])[1]").text]
        # print(original_message)
        #
        # for records in original_message:
        #     original_confirmation.append(records)
        # print(original_confirmation)
        #
        # assert original_message == original_confirmation