from get_serial_numbers import get_serial_numbers
import pytest


@pytest.mark.parametrize("a,expected", [
    ('0/L1.BIN', 261758686),
    ('0/L2.BIN', 261758686),
    ('0/L3.BIN', 261758686),
    ('0/L4.BIN', 261758686),
    ('100/L100.BIN', 261758686),
    ('100/L105.BIN', 261758686),
    ('100/L107.BIN', 261758686),
    ('100/L101.BIN', 261758686),
])
def test_get_serial_numbers(a, expected):
    path = '/Users/clarkbulleit/Desktop/Class Folders/' \
           'Medical Software/Projects/bme590final/Test_BIN/'
    file = path + a

    assert get_serial_numbers(file) == expected
