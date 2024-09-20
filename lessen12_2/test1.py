import pytest
from main import count_vowels

def test_all_vowels():
    assert count_vowels("aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ") == 30  #  "ё"


def test_no_vowels():
    assert count_vowels("bcdfgBCDFGбвгджзБВГДЖЗ") == 0

def test_mixed_string():
    assert count_vowels("Привет, мир! Hello, world!") == 6
    assert count_vowels("Python Программирование") == 8

if __name__ == '__main__':
    pytest.main()
