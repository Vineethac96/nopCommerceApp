import time
import pytest
from PageObjects.LoginPage import LoginPage  #we need to login as well
from PageObjects.searchCustomer import SearchCustomer
from Utilities.customLogger import LogGen
from Configurations.config import TestData

class Test_SearchCustomerByEmail_004:

    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver=setup
        self.driver.get(TestData.BaseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(TestData.Username)
        self.lp.setPassword(TestData.Password)
        self.lp.do_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        #self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
        self.driver.close()

