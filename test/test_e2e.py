import pytest

import xdist



from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckOutPge
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.Homepage import Homepage
from utility.Baseclass import Baseclass


class TestOne(Baseclass):

    def test_e2e(self):


        log = self.getLogger()
        homepage = Homepage(self.driver)
        checkOutpage = homepage.get_shopItem()


        # self.driver.find_element(By.CSS_SELECTOR,'a[href*="shop"]').click()

        checkOutpage = CheckOutPge(self.driver)
        products = checkOutpage.get_products()

        log.info("getting all the products")

        # products = self.driver.find_elements(By.XPATH,'//div[@class="card h-100"]')

        for product in products:
            productName = product.find_element(By.XPATH,'div/h4/a').text
            if productName=='Blackberry':
                product.find_element(By.XPATH,'div/button').click()

        # self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
        checkOutpage.get_Checkout_Items().click()

        confirmpage = checkOutpage.get_check_btn_success()
        # self.driver.find_element(By.XPATH,'//button[@class="btn btn-success"]').click()


        log.info("entering country name ind")
        confirmpage = ConfirmPage(self.driver)
        confirmpage.get_country().send_keys('Ind')
        # self.driver.find_element(By.ID,'country').send_keys('Ind')


        self.verify_link_presence('India')
        # wait = WebDriverWait(self.driver,10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

        confirmpage.get_country_Ind().click()
        # self.driver.find_element(By.LINK_TEXT,'India').click()

        confirmpage.get_checkbox().click()
        # self.driver.find_element(By.XPATH,'//div[@class="checkbox checkbox-primary"]').click()


        confirmpage.get_submit().click()
        # self.driver.find_element(By.XPATH,'//input[@type="submit"]').click()

        successText = self.driver.find_element(By.XPATH,'//div[@class="alert alert-success alert-dismissible"]').text

        assert 'Success!' in successText