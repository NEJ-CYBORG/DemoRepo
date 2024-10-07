import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PythonSelFramework.PageObjects.HomePage import HomePage
from PythonSelFramework.PageObjects.TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
        def test_formSubmission(self, getData):
            log = self.Getlogger()

#        driver.find_element(By.XPATH, "//input[@name='name']").send_keys("NeerajTried")
            homePage = HomePage(self.driver)
            log.info("the firstname is "+getData["firstname"])
            homePage.getName().send_keys(getData["firstname"])

#        driver.find_element(By.NAME, "email").send_keys("trying@yomail.com")
            homePage.getEmail().send_keys(getData["lastname"])

#        driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345678")
#            homePage.getpassword().send_keys(getData["password"])
#            homePage.clickRadio()

#        driver.find_element(By.ID, "exampleCheck1").click()
            homePage.clickCheck()

#        dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#        dropdown = Select(homePage.getList())
#        dropdown.select_by_index(0)
#        dropdown.select_by_visible_text("Male")
            self.SelectOptionbyText(homePage.getList(),getData["gender"])



#        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Heyyo")
#            homePage.getMsg().send_keys(getData["lmsg"])

#            homePage.getMsg().clear()

#        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
            homePage.submitclick()

            message = homePage.getAlertStatus().text
        # print(message)

            assert "Success" in message

            time.sleep(2)
            self.driver.refresh()

        @pytest.fixture(params=HomePageData.getTestData("t3"))
        def getData(self, request):
                return request.param
