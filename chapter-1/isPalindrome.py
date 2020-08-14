import pytest
from collections import defaultdict


def isPalindrome(string):
    nospace_string = string.replace(' ', '')
    letter_count = defaultdict(int)
    for char in nospace_string:
        letter_count[char] += 1

    num_lc_odd = 0
    for lc in letter_count.values():
        if lc % 2 == 1:
            num_lc_odd += 1

    if num_lc_odd > 1:
        return False

    if len(nospace_string) % 2 == 0:
        return num_lc_odd == 0
    else:
        return num_lc_odd == 1


def test_isPalindrome():
    assert isPalindrome('tact coa') == True
    assert isPalindrome('tac tca') == True
    assert isPalindrome('tact boa') == False
    assert isPalindrome('tac bca') == False
