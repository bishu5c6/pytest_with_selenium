import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser =="edge":
        # This force-downloads the correct driver and returns the local path
        # service = EdgeService(EdgeChromiumDriverManager().install())
        # driver = webdriver.Edge(service=service)
        driver = webdriver.ChromiumEdge()
    elif browser =="firefox":
        driver = webdriver.Firefox()
    return driver

#we are writing below code to run parameters from command prompt
def pytest_addoption(parser):
    parser.addoption("--browser") #this will get the value from CLI

@pytest.fixture()
def browser(request): #this will return the browser value to setup method
    return request.config.getoption("--browser")

#It is a hook for adding in the Html report
#customizing HTML Report
# def pytest_html_report_title(report):
#     report.title = "Testing"
#     report.title = " Login"
#     report.title= "Biswanth"
#
# # it is a hook for delete/modify into the HTML report.
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

# 1. Hook to set the Report Title (For pytest-html 4.0+)
def pytest_html_report_title(report):
    report.title = "Biswanth's Test Report"


# 2. This is the SPECIFIC hook for adding/removing Environment rows
def pytest_metadata(metadata):
    # ADDING new data
    metadata['Project Name'] = 'Orange HRM Login'
    metadata['Tester'] = 'Biswanth'

    # REMOVING (POP) unwanted data
    # We use .pop(key, None) so the code doesn't crash if the key is already gone
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)  # Example: remove platform if not needed

# 3. Optional: Hook to add specific summary text to the report
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["<p>Test Suite: Regression Login Flow</p>"])
