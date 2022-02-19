import requests
import pytest

from hamcrest import assert_that, equal_to

@pytest.mark.parametrize("url", ["https://www.google.com", "https://www.facebook.com"])
def test_website_is_ok(url):
    response = requests.get(url)
    
    assert_that(response.status_code, equal_to(200))