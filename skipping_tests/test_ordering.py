import pytest


class Test_Methods:

    def test_methodA(self):
        print("This is test methodA")

    def test_methodB(self):
        print("This is test methodB")

    def test_methodC(self):
        print("This is test methodC")


    @pytest.mark.second
    def test_methodD(self):
        print("This is test methodD")
    @pytest.mark.third
    def test_methodE(self):
        print("This is test methodE")

    # @pytest.mark.first
    @pytest.mark.run(order=1)
    def test_methodF(self):
        print("This is test methodF")


