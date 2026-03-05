import pytest

class Test_Class:

    @pytest.mark.dependency()
    def test_openapp(self):
        # print("This is test method1")
        assert False
    @pytest.mark.dependency(depends=['TestClass::test_openapp'])
    def test_login(self):
        # print("this method is used for login")
        assert True
    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_search(self):
        assert True
    @pytest.mark.dependency(depends=['TestClass::search','TestClass::test_login'])
    def test_advsearch(self):
        assert True
    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_logut(self):
        assert True
