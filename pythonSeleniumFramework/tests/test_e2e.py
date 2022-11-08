from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.TradePage import TradePage
from testLoginData.TestLoginData import TestData
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):
    def test_end_to_end(self, data_load):
        self.driver.get("https://trade.thinkorswim.com")
        login = LoginPage(self.driver)
        login.get_username().send_keys(data_load["username"])
        login.get_password().send_keys(data_load["password"])
        login.get_remember_user_id().click()
        login.get_login_button().click()

        trade = TradePage(self.driver)
        trade.get_search_box().send_keys("AAPL")
        trade.get_symbol().click()
        trade.get_buy_button().click()
        trade.get_quantity_input().click()
        for i in range(3):
            trade.get_quantity_input().send_keys(Keys.BACK_SPACE)
        trade.get_quantity_input().send_keys(2)
        trade.get_order_type().click()
        trade.get_market_order().click()
        trade.get_review_order().click()
        trade.get_send_order().click()
        trade.get_notification().click()
        trade.get_order_confirmation()
        sleep(2)
        trade.get_logout().click()

    @pytest.fixture(params=TestData.test_data)
    def data_load(self, request):
        return request.param




        # self.driver.find_element(By.XPATH, "//div[text()='Notifications']").click()
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
