import inspect
import logging


import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class Baseclass:

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('C:\\Users\\nik54\\PycharmProjects\\Automationproject123\\Logs\\logfile.log')
        formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)

        return logger







    def verify_link_presence(self,text):
        element= WebDriverWait(self.driver, 10).until(
        expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


    def select_By_Option(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
