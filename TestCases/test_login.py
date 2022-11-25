import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Configurations.config import TestData
from Utilities.customLogger import LogGen


class Test_001_login:     #test name

    # baseURL="https://admin-demo.nopcommerce.com/admin/"
    # username="admin@yourstore.com"
    # password="admin"
    #instaed of hardcoding common/test data here, create a config file in configuration folder and use it here,
    # so any change to input test data can be modified there in that file than in test file

    logger = LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression    #user defined markers,(built-in: xfail,skip,parameterize,usefixtures,skipif)
    def test_homePageTitle(self, setup): #using fixtures which has setup code and passing it as argument

        self.driver = setup  #passing driver through fixtures
        self.logger.info("****Opening URL****")
        self.driver.get(TestData.BaseURL)
        act_title = self.driver.title

        if act_title == TestData.Login_pge_tile:
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png") # if tsetcase fails
            self.driver.close()
            assert False

    @pytest.mark.sanity         #pytest -v -s -n 2 -m sanity --html=Reports\Reports.html .\TestCases\test_login.py --browser chrome
    def test_login(self,setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(TestData.BaseURL)
        self.lp=LoginPage(self.driver)  #create an instance/object of LoginPage Class to access its methods
        self.lp.setUsername(TestData.Username)
        self.lp.setPassword(TestData.Password)
        self.lp.do_login()

        act_title=self.driver.title
        if act_title==TestData.HomePage_title:
            self.logger.info("****Login test passed ****")
            # self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            # self.driver.close()
            assert False