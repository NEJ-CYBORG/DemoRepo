from selenium.webdriver.support.wait import WebDriverWait

from PythonSelFramework.PageObjects.ConfirmPage import ConfirmPage
from PythonSelFramework.PageObjects.HomePage import HomePage
from PythonSelenium.e2eTest import answer
from utilities.BaseClass import BaseClass
#@pytest.mark.usefixtures("setup")




class TestOne(BaseClass):
    def test_e2e(self):
        log = self.Getlogger()
#   Navigating from HomePage to Shop page
#        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        homePage = HomePage(self.driver)
        checkoutItem = homePage.shopItems()
        log.info("getting all card titles")


#   Adding Blackberry product to Cart
#      mobiles = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
#        checkOutPage = CheckOutPage(self.driver)
#        checkOutPage.ClickOnProd()
        checkoutItem.ClickOnProd()

#        for mobile in mobiles:
#            productName = mobile.find_element(By.XPATH, "div/h4/a").text
#            if productName == "Blackberry":
#                mobile.find_element(By.XPATH, "div/button").click()

        #    if "Blackberry" == mobile.text:
        #       driver.find_element(By.XPATH,"div/h4/a").click()
# Clicking on Cart

#        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
#        time.sleep(4)
#        Cartclick = CheckOutPage(self.driver)
        checkoutItem.Cart()


#   CLicking on inside the Cart
#        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
#        InCartClick = InCart(self.driver)
        location = ConfirmPage(self.driver)

        # switching to location page

        # passing 'india' as text
#        self.driver.find_element(By.ID, "country").send_keys("Ind")
#        places = ConfirmPage(self.driver)
#        places.placeName()
#       location.placeName()



        # waiting for the suggestions to show up
        wait = WebDriverWait(self.driver, 10)

        # selecting from suggestions
#        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
#        suggestions = ConfirmPage(self.driver)
        location.location_wait()

#        self.driver.find_element(By.LINK_TEXT, "India").click()
#        selection = ConfirmPage(self.driver)
        location.location_select()

        # switching to final screen
#        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
#        submission = ConfirmPage(self.driver)
        location.submit_button()

#       Printing the success message
#        answer = self.driver.find_element(By.CLASS_NAME, "alert-success").text
#        print(answer)
#        answer = ConfirmPage(self.driver)
        log.info("text match "+answer)
        print(location.success_message())
        # driver.get_screenshot_as_file("testing.png")