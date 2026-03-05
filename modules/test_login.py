import pytest


class TestLogin:
    def test_loginbyEmail(self,setup):
        print("Login by test email")
        assert 1==1

    def test_loginbyfacebook(self,setup):
        print("Login by facebook email")
        assert 1==1

    def test_loginbytwitter(self,setup):
        print("Login by twitter ")
        assert 1==1