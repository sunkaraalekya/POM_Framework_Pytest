from selenium import webdriver
import pytest
from pages.loginpage import login
from pages.homepage import Homepage

@pytest.mark.usefixtures("test_setup")
class TestLogin:

    # @pytest.fixture(scope='session')
    # def test_setup(self):
    #     global driver
    #     driver=webdriver.Chrome()
    #     driver.get("http://localhost:8080/login?from=%2F")
    #     driver.maximize_window()
    #     driver.implicitly_wait(30)
    #     yield
    #     driver.quit()

    def test_login(self):
        driver=self.driver
        lp=login(driver)
        lp.enter_un()
        lp.enter_pwd()
        lp.click_on_login_btn()

        # driver.find_element_by_name("j_username").send_keys("admin")
        # driver.find_element_by_name("j_password").send_keys("manager")
        # driver.find_element_by_name("Submit").click()


    def test_logout(self):
        driver=self.driver
        lp=Homepage(driver)
        lp.click_on_logout_btn()
        # driver.find_element_by_xpath("//*[text()='log out']").click()

