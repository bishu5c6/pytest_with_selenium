from selenium import webdriver
from selenium.webdriver.common.by import By

# class TestCLI:
#     def test_Login(self):
#         self.driver=webdriver.Chrome()
#         self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#         self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
#         self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
#         self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
#         try:
#             self.status = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']]").is_displayed()
#             self.driver.close()
#             assert self.status == True
#         except:
#             self.driver.close()
#             assert False
#
driver= webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
try:
    status = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']]").is_displayed()
    driver.close()
    assert status == True
except:
    driver.close()
    assert False