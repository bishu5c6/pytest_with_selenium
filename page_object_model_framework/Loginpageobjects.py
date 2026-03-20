from selenium import webdriver
from selenium.webdriver.common.by import By


class loginPage:
    #locators
    textbox_username_id ="username"
    textbox_password_id ="password"
    button_submit_xpath ="//button[@id='submit']"
    #constructors

    def __init__(self, driver):
        self.driver = driver





    #actions
    def setUsername(self, username):
        usernametxt=self.driver.find_element(By.ID,self.textbox_username_id)
        usernametxt.clear()
        usernametxt.send_keys(username)

    def setpwd(self, pwd):
        userpwd=self.driver.find_element(By.ID,self.textbox_password_id)
        userpwd.clear()
        userpwd.send_keys(pwd)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_submit_xpath).click()


#locators
#constructors
#action methods