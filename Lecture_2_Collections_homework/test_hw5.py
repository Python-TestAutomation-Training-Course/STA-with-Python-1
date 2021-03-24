import string

import pytest

from hw5 import custom_range


@pytest.mark.parametrize(
    "given, expected",
    [
        ([string.ascii_lowercase, "g"], ["a", "b", "c", "d", "e", "f"]),
        (
            [string.ascii_lowercase, "g", "p"],
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ([string.ascii_lowercase, "p", "g", -2], ["p", "n", "l", "j", "h"]),
        ([["a", "b", "c", "d", "e", "f", "g"], "d"], ["a", "b", "c"]),
        ([("a", "b", "c", "d", "e", "f", "g"), "d"], ["a", "b", "c"]),
    ],
)
def test_custom_range(given, expected):
    assert custom_range(*given) == expected


def test_positional_only():
    with pytest.raises(TypeError) as err:
        _ = custom_range("abc", start="a", stop="b", step=1)
    assert "got an unexpected keyword argument" in str(err.value)
