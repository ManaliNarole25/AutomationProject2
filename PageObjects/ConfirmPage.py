from selenium.webdriver.common.by import By


class ConfirmPage:
    Country = (By.ID, 'country')
    Country_Ind= (By.LINK_TEXT, 'India')
    Checkbox = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
    submit = (By.XPATH, '//input[@type="submit"]')

    def __init__(self,driver):
        self.driver = driver


    def get_country(self):
        return self.driver.find_element(*ConfirmPage.Country)

    def get_country_Ind(self):
        return self.driver.find_element(*ConfirmPage.Country_Ind)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.Checkbox)


    def get_submit(self):
        return self.driver.find_element(*ConfirmPage.submit)








