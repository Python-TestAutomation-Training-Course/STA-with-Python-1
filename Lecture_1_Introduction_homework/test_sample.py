import pytest


def test_pass():
    """This test should pass"""
    assert True


def get_length(test_string):
    """Return length of the string"""
    return len(test_string)


@pytest.mark.parametrize("test_string,result", [("test", 4), ("\t", 1)])
def test_string_length(test_string, result):
    assert get_length(test_string) == result


def remove_spaces(test_string):
    """Removes spaces, tabs for the string"""
    return test_string.strip()


@pytest.mark.parametrize("test_string,result", [("test", "test"), ("\ttab", "tab"), ("  whitespace ", "whitespace")])
def test_string_remove_spaces(test_string, result):
    assert remove_spaces(test_string) == result
