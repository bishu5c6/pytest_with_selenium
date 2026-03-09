import pytest


class TestClass:
    @pytest.mark.sanity
    def test_loginbyEmail(self):
        print("testing is done by email: ")
        assert 1==1
    @pytest.mark.sanity
    def test_loginbyfacebook(self):
        print("testing is done by facebook")
        assert 1==1
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginbytwitter(self):
        print("testing is done by twittwe: ")
        assert 1==1
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_signupbyEmail(self):
        print("signup is done by email: ")
        assert 1==1
    @pytest.mark.regression
    def test_signupbyfacebook(self):
        print("signup is done by facebook")
        assert 1==1
    @pytest.mark.regression
    def test_signupbytwitter(self):
        print("signup is done by twittwe: ")
        assert 1==1


