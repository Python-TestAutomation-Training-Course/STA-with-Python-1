import pytest 
import requests

from requests.exceptions import ConnectionError
from hamcrest import assert_that, equal_to

@pytest.mark.foobar
def test_google_is_ok():
    response = requests.get("https://www.google.com")
    
    assert_that(response.status_code, equal_to(200))
    
    
def test_facebook_is_ok():
    response = requests.get("https://www.facebook.com")
    
    assert_that(response.status_code, equal_to(200))
    

def test_hello_failing_google():
    response = requests.get("https://www.google.com")
    assert_that(response.status_code, equal_to(500))