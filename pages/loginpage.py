import testdata.constants as Dataval
class login:
    def __init__(self,driver):
        self.driver=driver
        self.un_txt_bx_name='j_username'
        self.pwd_txt_bx_name='j_password'
        self.login_btn_name ='Submit'
        # self.logout_btn_name="//*[text()='log out']"

    def enter_un(self):
        self.driver.find_element_by_name(self.un_txt_bx_name).send_keys(Dataval.UN)

    def enter_pwd(self):
        self.driver.find_element_by_name(self.pwd_txt_bx_name).send_keys(Dataval.PWD)

    def click_on_login_btn(self):
        self.driver.find_element_by_name(self.login_btn_name).click()

    # def click_on_logout_btn(self):
    #     self.driver.find_element_by_xpath(self.logout_btn_name).click()