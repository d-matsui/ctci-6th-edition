import pytest


def isSameByEdittingOnce(str_a, str_b):
    # check if two strings can be same by editting (insert, remove and replace) once
    # assume len(str_a) > len(str_b)
    if len(str_a) < len(str_b):
        str_a, str_b = str_b, str_a

    diff_length = len(str_a) - len(str_b)

    if diff_length >= 2:
        return False
    elif diff_length == 1:
        # case of removing or inserting
        for i in range(len(str_a)):
            if str_a[:i] + str_a[i+1:] == str_b:
                return True
        return False
    else:
        # case of replacing
        replace_count = 0
        for i in range(len(str_a)):
            char_a, char_b = str_a[i], str_b[i]
            if char_a != char_b:
                replace_count += 1
                if replace_count >= 2:
                    return False
        return True


def test_isSameByEdittingOnce():
    assert isSameByEdittingOnce('pale', 'pale') == True
    assert isSameByEdittingOnce('pales', 'pale') == True
    assert isSameByEdittingOnce('palo', 'pale') == True

    assert isSameByEdittingOnce('pale', 'polo') == False
    assert isSameByEdittingOnce('pales', 'pole') == False
    assert isSameByEdittingOnce('palese', 'pale') == False

