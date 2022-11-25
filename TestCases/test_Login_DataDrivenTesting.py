import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Configurations.config import TestData
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import time


class Test_002_DDT_login:     #test name

    path= TestData.Datafile_Path
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_DDT(self,setup):

        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(TestData.BaseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)  #creating object

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)

        lst_status = []           # we create an empty lost variable to store the pass/fail results in an array for the data in excel
                                  # and then based on this we can say our entire TC is pass or fail

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.do_login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = TestData.HomePage_title

            if act_title == exp_title: #1st verify title
                if self.exp == "Pass":
                   self.logger.info("**** passed ****")
                   self.lp.do_logout();#logout for next test
                   lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** failed ****")
                    self.lp.do_logout();
                    lst_status.append("Fail")

            else:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
                self.logger.info("******* DDT Login test passed **********")
                self.driver.close()
                assert True
        else:
                self.logger.error("******* DDT Login test failed **********")
                self.driver.close()
                assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");




