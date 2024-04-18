from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPge:

    products = (By.XPATH,'//div[@class="card h-100"]')
    checkout = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    checkout_btn_success = (By.XPATH, '//button[@class="btn btn-success"]')

    def __init__(self,driver):
        self.driver = driver

    def get_products(self):
       return self.driver.find_elements(*CheckOutPge.products)

    def get_Checkout_Items(self):
        return self.driver.find_element(*CheckOutPge.checkout)

    def get_check_btn_success(self):
        self.driver.find_element(*CheckOutPge.checkout_btn_success).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage



