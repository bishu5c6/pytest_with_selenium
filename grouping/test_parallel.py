import pytest



class TestParallel:
    def test_chrome(self):
        try:
            print("testing is done by chrome: ")
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            self.driver = webdriver.Chrome
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
            self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
            assert self.driver.title == "OrangeHRM"
            self.driver.quit()
        except Exception as e:
            print(e,"browser not available in your system")

    def test_edge(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        options = webdriver.EdgeOptions()
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_firefox(self):
        try:
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            self.driver = webdriver.Firefox()
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
            self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
            assert self.driver.title == "OrangeHRM"
            self.driver.quit()
        except Exception as e:
            print(e,"browser not available in your system")