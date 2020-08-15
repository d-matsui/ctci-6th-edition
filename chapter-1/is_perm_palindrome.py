import pytest
from collections import defaultdict


# O(N)
def is_perm_palindrome(string):
    # check if a string is a permutation of a palindrome or not
    nospace_lower_string = string.replace(' ', '').lower()
    table = build_char_frequency_table(nospace_lower_string)
    return check_max_one_odd(table)


def build_char_frequency_table(string):
    char_frequency_table = defaultdict(int)

    for char in string:
        char_frequency_table[char] += 1

    return char_frequency_table


def check_max_one_odd(table):
    num_odds = 0
    for char_frequency in table.values():
        if char_frequency % 2 == 1:
            num_odds += 1
            if num_odds > 1:
                return False

    return True


# optimization by creating char_freq_table and counting num_odds simultaneously
def check_max_one_odd_optimized(string):
    char_frequency_table = defaultdict(int)
    num_odds = 0

    for char in string:
        char_frequency_table[char] += 1
        if char_frequency_table[char] % 2 == 1:
            num_odds += 1
        else:
            num_odds -= 1

    return num_odds <= 1


# TODO: optimization by using a bit vector which maps a character to an integer


def test_is_perm_palindrome():
    assert is_perm_palindrome('tact coa') == True
    assert is_perm_palindrome('tAc tca') == True
    assert is_perm_palindrome('tact boa') == False
    assert is_perm_palindrome('tac bca') == False
