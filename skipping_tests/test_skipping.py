import pytest

class Test_loging:
    def test_email(self):
        print("Done testing using email")
        assert 1==1

    def test_facebook(self):
        print("testing done by using facebook")
        assert 1==1

    @pytest.mark.skip
    def test_twitter(self):
        print("testing done by using email")
        assert 1==0


