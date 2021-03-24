import pytest

from hw2 import major_and_minor_elem


@pytest.mark.parametrize(
    "numbers, expected", [([2, 2, 1, 1, 1, 2, 2], (2, 1)), ([3, 2, 3], (3, 2))]
)
def test_hw2(numbers, expected):
    assert major_and_minor_elem(numbers) == expected
