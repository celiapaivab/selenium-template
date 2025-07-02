from pages.login_page import LoginPage

def test_login_sucesso(driver, base_url):
    driver.get(base_url)
    login_page = LoginPage(driver)
    
    login_page.enter_username("usuario_teste")
    login_page.enter_password("senha123")
    login_page.click_login()
    
    assert "Página Inicial" in driver.title
