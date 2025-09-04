from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "loginBtn")

    # Open the login page
    def open(self, url):
        self.driver.get(url)

    # Enter the username
    def enter_username(self, username):
        element = self.driver.find_element(*self.username_input)
        element.clear()
        element.send_keys(username)

    # Enter the password
    def enter_password(self, password):
        element = self.driver.find_element(*self.password_input)
        element.clear()
        element.send_keys(password)

    # Click the login button
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    # Combine username, password, and click login
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
