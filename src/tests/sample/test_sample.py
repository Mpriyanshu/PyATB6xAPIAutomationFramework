import pytest
import allure

@allure.title("Verify ❌ Failed ! that the Framework is working")
def test_sample_pass():
    assert True == False


@allure.title("Verify ✅ Passed that the Framework is working")
def test_sample_fail():
    assert True == True
