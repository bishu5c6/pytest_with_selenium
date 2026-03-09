import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

class TestLoging:
    @pytest.mark.parametrize('uname, upassword',[('Admin','admin123'),('pilli','pilli123')])
    def test_login(self, uname,upassword):

        self.driver = webdriver.Chrome()
        try:
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(uname)
            self.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(upassword)
            self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
            self.driver.status = self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status == True
            time.sleep(5)

        except:
            self.driver.close()
            assert False