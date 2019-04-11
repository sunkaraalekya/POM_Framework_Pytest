class Homepage:
    def __init__(self,driver):
        self.driver=driver
        self.logout_btn_name = "//*[text()='log out']"

    def click_on_logout_btn(self):
        self.driver.find_element_by_xpath(self.logout_btn_name).click()