


import pytest
from selenium import webdriver

#example-1:
@pytest.fixture()
def setup():
    print("Launching browser: ")


# @pytest.fixture()
# def setup(browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "edge":
#         driver = webdriver.Edge()
#     else:
#         driver = webdriver.Firefox()
#
#     yield driver  # Provides the driver to the test
#     driver.quit()  # Cleanup (Post-test execution)
#
# def pytest_addoption(parser):    # This will get the value from CLI
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):       # This will return the Browser value to setup method
#     return request.config.getoption("--browser")