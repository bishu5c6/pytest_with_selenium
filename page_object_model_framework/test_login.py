import time

from selenium import webdriver
from Loginpageobjects import loginPage
import time
class TestLogin:
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()


        self.lp=loginPage()
        self.lp.setUsername("student")
        self.lp.setpwd("Password123")
        self.lp.clicklogin()
        time.sleep(4)
        self.act_title=self.driver.title
        assert self.act_title=="Test Login | Practice Test Automation"

        