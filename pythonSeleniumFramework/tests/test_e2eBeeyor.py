from time import sleep
from selenium.webdriver import ActionChains, Keys
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.OrderPage import OrderPage
from pageObjects.ShoppingPage import ShoppingPage
from utilities.BaseClass import BaseClass


class TestE2EBeeyor(BaseClass):

    def test_e2e_beeyor(self, data_load_beeyor):
        self.driver.get("http://shopping.beeyor.com/shop")
        checkout_window = self.driver.window_handles
        shopping = ShoppingPage(self.driver)
        items = shopping.get_list_of_items()
        for item in items:
            item.click()
            if item == self.driver.find_element(*ShoppingPage.last_element):
                break
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*ShoppingPage.cart)).perform()
        sleep(2)
        action.move_to_element(self.driver.find_element(*ShoppingPage.view_cart)).click().perform()

        order = OrderPage(self.driver)
        order.get_quantity_change().click()
        order.get_quantity_change().send_keys(Keys.COMMAND + "a")
        order.get_quantity_change().send_keys("3")
        order.get_coupon().send_keys(data_load_beeyor["coupon"])
        order.get_apply_coupon().click()
        order.get_checkout_button().click()

        billing = CheckoutPage(self.driver)
        billing.get_billing_firstname().send_keys(data_load_beeyor["firstname"])
        billing.get_billing_lastname().send_keys(data_load_beeyor["lastname"])
        billing.get_billing_street().send_keys(data_load_beeyor["street"])
        billing.get_billing_city().send_keys(data_load_beeyor["city"])
        billing.get_billing_postcode().send_keys(data_load_beeyor["postcode"])
        billing.get_billing_phone().send_keys(data_load_beeyor["phone"])
        billing.get_billing_email().send_keys(data_load_beeyor["email"])
        billing.get_frame_1()
        billing.get_card_number().send_keys(data_load_beeyor["cardnumber"])
        self.driver.switch_to.window(checkout_window[0])
        billing.get_frame_2()
        billing.get_expiration_date().send_keys(data_load_beeyor["expdate"])
        self.driver.switch_to.window(checkout_window[0])
        billing.get_frame_3()
        billing.get_cvc_code().send_keys(data_load_beeyor["cvc"])
        self.driver.switch_to.window(checkout_window[0])
        billing.get_place_order().click()
