import pytest


def compress(string):
    compressed_string = ''
    index = 0
    while index <= len(string) - 1:
        index, char, num = search(string, index)
        compressed_string += f'{char}{num}'
        if len(compressed_string) >= len(string):
            compressed_string = string
            break

    return compressed_string


def search(string, index):
    char = string[index]
    num = 1
    if index == len(string) - 1:
        return index + 1, char, num
    index += 1

    next_char = string[index]
    while next_char == char:
        index += 1
        num += 1
        if index > len(string) - 1:
            break
        next_char = string[index]

    return index, char, num


def test_compress():
    assert compress('abc') == 'abc'
    assert compress('aabbcc') == 'aabbcc'
    assert compress('aabbbcc') == 'a2b3c2'
