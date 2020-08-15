import pytest


def one_away(str_a, str_b):
    # check if a string can be converted to another string with a single edit
    diff_length = abs(len(str_a) - len(str_b))

    if diff_length == 0:
        return one_edit_replace(str_a, str_b)
    elif diff_length == 1:
        return one_edit_remove(str_a, str_b)
    else:
        return False


def one_edit_replace(str_a, str_b):
    # assume len(str_a) >= len(str_b)
    if len(str_a) < len(str_b):
        str_a, str_b = str_b, str_a

    edited = False
    for char_a, char_b in zip(str_a, str_b):
        if char_a != char_b:
            if edited:
                return False
            edited = True
    return True


def one_edit_remove(str_a, str_b):
    for i in range(len(str_a)):
        if str_a[:i] + str_a[i+1:] == str_b:
            return True
    return False


def test_one_away():
    assert one_away('pale', 'pale') == True
    assert one_away('pales', 'pale') == True
    assert one_away('palo', 'pale') == True

    assert one_away('pale', 'polo') == False
    assert one_away('pales', 'pole') == False
    assert one_away('palese', 'pale') == False
