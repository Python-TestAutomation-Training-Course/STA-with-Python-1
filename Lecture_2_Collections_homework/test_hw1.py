import os
from tempfile import NamedTemporaryFile

import pytest

from hw1 import check_data, validate_date, validate_line

data = [
    "baz@example.com 729.83 USD accountName 2021-01-02",
    "foo@example.com 729.83 EUR accountName 2021-01:0",
    "bar@example.com 729.83 accountName 2021-01-02",
    "baz@example.com 729.83 USD accountName ABCD-01-02",
    "baz@example.com 729.83 USD accountName 2021--02",
    "baz@example.com 729.83 USD accountName 2021:01:02",
    "baz@example.com 729.83 USD 2021-01-",
    "baz@example.com 729.83 USD accountName !!!:{{:{{",
    "2021-01-02",
]


@pytest.fixture
def file_path():
    tp = NamedTemporaryFile(mode="a")
    for line in data:
        tp.write(line + "\n")
        tp.flush()

    yield tp.name
    tp.close()
    os.remove(os.path.abspath("result.txt"))


def test_hw1(file_path):
    result_path = check_data(file_path, [validate_date, validate_line])
    with open(result_path) as res:
        for i, line in enumerate(res, start=1):
            assert line.rsplit(" ", 1)[0] in data

    assert i == len(data) - 1


def test_real_file():
    result_path = check_data("data.txt", [validate_date, validate_line])
    with open(result_path) as res:
        for i, _ in enumerate(res, start=1):
            pass
    assert i == 777
