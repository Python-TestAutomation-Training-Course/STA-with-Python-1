import pytest

from bad import create_country_make_dict as bad_dict
from good import create_country_make_dict as good_dict

REQUEST_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json"


@pytest.mark.parametrize("dict_func", [bad_dict, good_dict])
def test_dict_length(dict_func):
    dict_length = len(dict_func(REQUEST_URL))
    assert dict_length == 79, f"Expected length to be 79, but got {dict_length} instead"
