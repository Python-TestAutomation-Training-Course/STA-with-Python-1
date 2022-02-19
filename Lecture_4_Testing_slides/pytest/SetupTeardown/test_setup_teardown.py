import requests
from hamcrest import assert_that, equal_to

def test_google_is_ok():
    response = requests.get("https://www.google.com")
    
    assert_that(response.status_code, equal_to(200))
 
 
def test_facebook_is_ok():
    response = requests.get("https://www.facebook.com")
    
    assert_that(response.status_code, equal_to(200))