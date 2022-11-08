from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
    username = (By.ID, "username0")
    password = (By.ID, "password1")
    remember_user_id = (By.XPATH, "//label[@for='rememberuserid']")
    login_button = (By.CLASS_NAME, "accept")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_remember_user_id(self):
        return self.driver.find_element(*LoginPage.remember_user_id)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

