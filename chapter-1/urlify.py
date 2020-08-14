import pytest


# O(N)
def urlify(string, length):
    # replace spaces with %20 and remove trailing spaces
    string_list = list(string)
    index = len(string_list)

    for i in reversed(range(length)):
        if string_list[i] == ' ':
            # replace spaces
            string_list[index - 3:index] = '%20'
            index -= 3
        else:
            # move characters
            string_list[index - 1] = string_list[i]
            index -= 1

    return ''.join(string_list)


def test_urlify():
    assert urlify('Mr John Smith    ', 13) == 'Mr%20John%20Smith'
