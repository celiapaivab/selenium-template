from pages.login_page import LoginPage
from utils.data import BASE_URL, USERNAME, PASSWORD


def test_login_success(driver):
    # Initialize the login page object
    login_page = LoginPage(driver)

    # Open the login page
    login_page.open(BASE_URL)

    # Enter username and password, then click login
    login_page.login(USERNAME, PASSWORD)

    # Verify that login was successful by checking the page title
    assert "Home Page" in driver.title
