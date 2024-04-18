import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.Homepage import Homepage
from TestData.HomePageTestData import HomePaageTestData
from utility.Baseclass import Baseclass


class TestHomePage(Baseclass):

    def test_formSubmission(self,getdata):
        homepage = Homepage(self.driver)
        homepage.get_name().send_keys(getdata["name"])
        # self.driver.find_element(By.XPATH,'(//input[@name="name"])[1]').send_keys('Rahul')

        homepage.get_email().send_keys(getdata["email"])
        # self.driver.find_element(By.NAME, 'email').send_keys('hello@gmail.com')

        homepage.get_password().send_keys(getdata["password"])
        # self.driver.find_element(By.ID, 'exampleInputPassword1').send_keys(123456)

        homepage.get_example_check().click()
        # self.driver.find_element(By.ID, 'exampleCheck1').click()

        homepage.get_option_value().click
        # self.driver.find_element(By.CSS_SELECTOR,'input[value="option1"]').click


        # sel = Select(homepage.get_gender())
        # sel.select_by_visible_text("Female")
        # dropdown = Select(self.driver.find_element(By.ID,'exampleFormControlSelect1'))
        # dropdown.select_by_index(0)
        # dropdown.select_by_visible_text('Female')


        homepage.get_submit().click()
        # self.driver.find_element(By.XPATH,'//input[@type="submit"]').click()

        homepage.get_alertText().text
        # message = self.driver.find_element(By.CLASS_NAME,"alert-success").text
        # print(message)
        # assert 'Success' in message

        self.driver.refresh()

    @pytest.fixture(params=HomePaageTestData. test_home_page_data)
    def getdata(self,request):
        return request.param


