import pytest


def is_unique(string):
    # assume character set is ASCCI (128 characters)
    if len(string) > 128:
        return False

    char_set = [False] * 128
    for char in string:
        index = ord(char)
        if char_set[index]:
            # char has already been found in string
            return False
        char_set[index] = True

    return True


def test_is_unique():
    assert is_unique('abc') == True
    assert is_unique('abca') == False
