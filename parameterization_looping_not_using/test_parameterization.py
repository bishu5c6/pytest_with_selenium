import pytest

class TestClass:
    @pytest.mark.parametrize('num1, num2',[(2,2),(3,3),(4,4),(9,7)]) #built in method
    def test_multiplication(self, num1, num2):
        assert num1==num2

