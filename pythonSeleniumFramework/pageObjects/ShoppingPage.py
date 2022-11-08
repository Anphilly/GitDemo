from selenium.webdriver.common.by import By


class ShoppingPage:

    def __init__(self, driver):
        self.driver = driver
    list_of_items = (By.XPATH, "//a[text()='Add to cart']")
    last_element = (By.XPATH, "(//a[text()='Add to cart'])[3]")
    cart = (By.XPATH, "(//span[@class='count'])[1]")
    view_cart = (By.XPATH, "//p/a[text()='View cart']")


    def get_list_of_items(self):
        return self.driver.find_elements(*ShoppingPage.list_of_items)

    def get_cart(self):
        return self.driver.find_element(*ShoppingPage.cart)

    def get_view_cart(self):
        return self.driver.find_element(*ShoppingPage.view_cart)




    # list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")
    # list_of_items.remove(driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[1]"))
    # list_of_items.remove(driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[4]"))
 # for item in list_of_items:
#         item.click()
#         if item == driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[5]"):
#             break
# action = ActionChains(driver)
#     action.move_to_element(driver.find_element(By.XPATH, "(//span[@class='count'])[1]")).perform()
#     action.move_to_element(driver.find_element(By.XPATH, "//p/a[text()='View cart']")).click().perform()
