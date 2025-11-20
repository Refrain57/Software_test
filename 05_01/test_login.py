import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import time

@allure.feature('用户登录模块')
class TestLoginProject:
    
    def setup_method(self):
        # -----------------------------------------
        # 👇 这里改了：把 Chrome() 改成 Edge()
        self.driver = webdriver.Edge() 
        # -----------------------------------------
        
        self.driver.maximize_window()
        # 打开练习网站
        self.driver.get("https://www.saucedemo.com/")

    @allure.story('用例1: 正常登录')
    def test_standard_login(self):
        driver = self.driver
        # 这里的代码完全不用动，因为 Edge 和 Chrome 是一样的内核
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        time.sleep(2) 
        assert "inventory" in driver.current_url

    @allure.story('用例2: 错误密码登录')
    def test_fail_login(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("wrong_pass")
        driver.find_element(By.ID, "login-button").click()
        
        error_msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert "Epic sadface" in error_msg

    def teardown_method(self):
        self.driver.quit()