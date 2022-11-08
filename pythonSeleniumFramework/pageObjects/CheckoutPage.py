from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
    billing_firstname = (By.ID, "billing_first_name")
    billing_lastname = (By.ID, "billing_last_name")
    billing_street = (By.XPATH, "(//input[@placeholder='House number and street name'])[1]")
    billing_city = (By.CSS_SELECTOR, "input[name='billing_city']")
    billing_postcode = (By.CSS_SELECTOR, "input[name='billing_postcode']")
    billing_phone = (By.CSS_SELECTOR, "input[name='billing_phone']")
    billing_email = (By.CSS_SELECTOR, "input[name='billing_email']")
    card_number = (By.XPATH, "//input[@name='cardnumber']")
    expiration_date = (By.CSS_SELECTOR, "input[name='exp-date']")
    cvc_code = (By.CSS_SELECTOR, "input[aria-label='Credit or debit card CVC/CVV']")
    place_order = (By.ID, "place_order")

    def get_billing_firstname(self):
        return self.driver.find_element(*CheckoutPage.billing_firstname)

    def get_billing_lastname(self):
        return self.driver.find_element(*CheckoutPage.billing_lastname)

    def get_billing_street(self):
        return self.driver.find_element(*CheckoutPage.billing_street)

    def get_billing_city(self):
        return self.driver.find_element(*CheckoutPage.billing_city)

    def get_billing_postcode(self):
        return self.driver.find_element(*CheckoutPage.billing_postcode)

    def get_billing_phone(self):
        return self.driver.find_element(*CheckoutPage.billing_phone)

    def get_billing_email(self):
        return self.driver.find_element(*CheckoutPage.billing_email)

    def get_frame_1(self):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@title='Secure card number input frame']"))
        return

    def get_card_number(self):
        return self.driver.find_element(*CheckoutPage.card_number)

    def get_frame_2(self):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@title='Secure expiration date input frame']"))
        return

    def get_expiration_date(self):
        return self.driver.find_element(*CheckoutPage.expiration_date)

    def get_frame_3(self):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@title='Secure CVC input frame']"))
        return

    def get_cvc_code(self):
        return self.driver.find_element(*CheckoutPage.cvc_code)

    def get_place_order(self):
        return self.driver.find_element(*CheckoutPage.place_order)





# driver.find_element(By.XPATH, "(//input[@placeholder='House number and street name'])[1]").send_keys(
#     ("2277 Main Street"))
# driver.find_element(By.CSS_SELECTOR, "input[name='billing_city']").send_keys("Manhattan")
# driver.find_element(By.CSS_SELECTOR, "input[name='billing_postcode']").send_keys("17177")
# driver.find_element(By.CSS_SELECTOR, "input[name='billing_phone']").send_keys("205-205-4455")
# driver.find_element(By.CSS_SELECTOR, "input[name='billing_email']").send_keys("tony_stark@starkcorp.com")
# driver.switch_to.frame(1)
# driver.find_element(By.XPATH, "//input[@name='cardnumber']").send_keys("4242424242424242")
# driver.find_element(By.CSS_SELECTOR, "input[name='exp-date']").send_keys("1125")
# # frame_element = driver.find_element(By.XPATH, "//iframe[@name='__privateStripeFrame4399']")
# driver.switch_to.window(checkout_window[0])
# driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Secure CVC input frame']"))
# driver.find_element(By.CSS_SELECTOR, "input[aria-label='Credit or debit card CVC/CVV']").send_keys("343")
# driver.switch_to.window(checkout_window[0])
# driver.find_element(By.ID, "place_order").click()
