from radix_sort import radix_int, radix_string
import pytest


def test_radix_int():
    list_1 = [0, 1, 2, 3, 4, 5]
    list_2 = [5, 4, 3, 2, 1, 0]
    list_3 = [2, 4, 3, 5, 0, 1]
    expected = [0, 1, 2, 3, 4, 5]
    assert radix_int(list_1) == expected
    assert radix_int(list_2) == expected
    assert radix_int(list_3) == expected
    #  These should come out to be the same


def test_radix_int_2():
    list_1 = [4355, 63255, 76532, 9, 000]
    list_2 = [000, 9, 4355, 63255, 76532]
    expected = [000, 9, 4355, 63255, 76532]
    assert radix_int(list_1) == expected
    assert radix_int(list_2) == expected


def test_radix_string():
    list_1 = ['a', 'aa', 'aab', 'b', 'bbc', 'x', 'y', 'z']
    list_2 = ['z', 'y', 'x', 'bbc', 'b', 'aab', 'aa', 'a']
    expected = ['a', 'aa', 'aab', 'b', 'bbc', 'x', 'y', 'z']
    assert radix_string(list_1) == expected
    assert radix_string(list_2) == expected


def test_radix_string_2():
    list_1 = ['qufygbrkg', 'adfbar', 'nvhdvh', 'zzzngybadadg']
    expected = ['adfbar', 'nvhdvh', 'qufygbrkg', 'zzzngybadadg']
    assert radix_string(list_1) == expected
