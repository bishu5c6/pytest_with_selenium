import pytest

class TestMethod:
    @pytest.fixture() #decorator
    def setup(self):
        print("Launching the browser .....")
        print("Opening the application")
        yield
        print("closing the browser")
    def testmethod1(self, setup):
        print("This is test method 1")
    def advance(self, setup):
        print("This advance method")
    def test_advance_method(self, setup):
        print("this is test advance method")

