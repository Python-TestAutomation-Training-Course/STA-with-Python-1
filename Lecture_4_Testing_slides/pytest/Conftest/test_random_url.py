import requests
from hamcrest import assert_that, equal_to

def test_random_website_is_ok(random_url):
    response = requests.get(random_url)
    
    assert_that(response.status_code, equal_to(200))