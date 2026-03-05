import pytest

@pytest.fixture()
def setup():
    print("Start of the code")
    yield
    print("ENd of the method")