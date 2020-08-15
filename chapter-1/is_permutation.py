import pytest
from collections import defaultdict

# O(N)
def is_permutation(str_a, str_b):
    if len(str_a) != len(str_b):
        return False

    count_str_a = defaultdict(int)
    count_str_b = defaultdict(int)

    for i in range(len(str_a)):
        count_str_a[str_a[i]] += 1
        count_str_b[str_b[i]] += 1

    if count_str_a == count_str_b:
        return True

    return False


def test_is_permutation():
    assert is_permutation('abc', 'cab') == True
    assert is_permutation('ab c', 'c ab') == True
    assert is_permutation('abc', 'Cab') == False
    assert is_permutation('ab c', 'cab') == False
