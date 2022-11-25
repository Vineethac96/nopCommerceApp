'''conftest.py has all the common initial setup process by using fixtures
Here, we are passing driver initiliaztion'''

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#the browser is designed at run time


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:                                              #default browser if not mentioned anything during pytest.....execution
        driver =  webdriver.Ie()
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method, *request* object
    return request.config.getoption("--browser")


#To run tests on desired browser, :(we are taking browser option from CLI
#   pytest -v -s <filename> --browser chrome
# pytest -v -s <filename> --browser firefox


#What Is Yield In Python? The Yield keyword in Python is similar to a return statement used for returning values or objects in Python. However, there is a slight difference. The yield statement returns a
# generator object to the one who calls the function which contains yield, instead of simply returning a value.