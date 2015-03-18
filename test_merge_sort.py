import merge_sort
import merge_sort as merge
import pytest


def test_sorted():
    sorted_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    merge.merge_sort(sorted_list)
    assert sorted_list == [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]


def test_unsorted():
    unsorted_list = [3, 100, 5, 76, -32, 3, 2, 444]
    merge.merge_sort(unsorted_list)
    assert unsorted_list == [-32, 2, 3, 3, 5, 76, 100, 444]


def test_empty():
    empty = []
    merge.merge_sort(empty)
    assert empty == []
