from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckOutPge


class Homepage:
    shop = (By.CSS_SELECTOR, 'a[href*="shop"]')
    name = (By.XPATH, '(//input[@name="name"])[1]')
    email = (By.NAME, 'email')
    password = (By.ID, 'exampleInputPassword1')
    checkbox = (By.ID, 'exampleCheck1')
    option_value = (By.CSS_SELECTOR, 'input[value="option1"]')
    gender = (By.ID,'exampleFormControlSelect1')
    submit = (By.XPATH,'//input[@type="submit"]')
    alerttext = (By.CLASS_NAME,"alert-success")


    def __init__(self,driver):
        self.driver = driver

    def get_shopItem(self):
        self.driver.find_element(*Homepage.shop).click()
        checkOutpage = CheckOutPge(self.driver)
        return checkOutpage

    def get_name(self):
        return self.driver.find_element(*Homepage.name)

    def get_email(self):
        return self.driver.find_element(*Homepage.email)

    def get_password(self):
        return self.driver.find_element(*Homepage.password)


    def get_example_check(self):
        return self.driver.find_element(*Homepage.checkbox)

    def get_option_value(self):
        return self.driver.find_element(*Homepage.option_value)

    def get_gender(self):
        return self.driver.find_element(*Homepage.gender)

    def get_submit(self):
        return self.driver.find_element(*Homepage.submit)

    def get_alertText(self):
        return self.driver.find_element(*Homepage.alerttext)




