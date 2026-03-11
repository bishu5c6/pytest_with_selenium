from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCLI:
    def test_logo(self, setup):
        self.driver = setup
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        try:
            self.status=self.driver.find_element(By.XPATH,"//h2[normalize-space()='Test login']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False


    def test_login(self, setup):
        # print(setup)#print return statement from the conftest.py
        self.driver = setup
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.find_element(By.XPATH,"//input[@id='username']").send_keys("student")
        self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Password123")
        self.driver.find_element(By.XPATH,"//button[@id='submit']").click()
        try:
            self.status = self.driver.find_element(By.XPATH,"//h1[normalize-space()='Logged In Successfully']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False