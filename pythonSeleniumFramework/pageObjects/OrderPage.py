from selenium.webdriver.common.by import By


class OrderPage:

    def __init__(self, driver):
        self.driver = driver
    quantity_change = (By.XPATH, "(//div/input[@type='number'])[1]")
    coupon = (By.CSS_SELECTOR, "#coupon_code")
    apply_coupon = (By.XPATH, "//button[text()='Apply coupon']")
    checkout_button = (By.CLASS_NAME, "checkout-button")

    def get_quantity_change(self):
        return self.driver.find_element(*OrderPage.quantity_change)

    def get_coupon(self):
        return self.driver.find_element(*OrderPage.coupon)

    def get_apply_coupon(self):
        return self.driver.find_element(*OrderPage.apply_coupon)

    def get_checkout_button(self):
        return self.driver.find_element(*OrderPage.checkout_button)


#     driver.find_element(By.XPATH, "(//div/input[@type='number'])[1]").send_keys(Keys.COMMAND + "a")
#     driver.find_element(By.XPATH, "(//div/input[@type='number'])[1]").send_keys("3")
#     driver.find_element(By.XPATH, "//button[text()='Update cart']").click()
#     wait = WebDriverWait(driver, 10)
#     wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@role='alert']")))
#     driver.find_element(By.CSS_SELECTOR, "#coupon_code").send_keys("Tojtech Automation")
#     sleep(2)
#     driver.find_element(By.XPATH, "//button[text()='Apply coupon']").click()
#     sleep(2)
#     wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='woocommerce-message']")))
#     sleep(2)
#     driver.find_element(By.CLASS_NAME, "checkout-button").click()
#     sleep(2)