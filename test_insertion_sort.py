import insertion_sort as insertion_sort


def test_sorted():
    sorted_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    insertion_sort.sort(sorted_list)
    assert sorted_list == [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]


def test_unsorted():
    unsorted_list = [3, 100, 5, 76, -32, 3, 2, 444]
    insertion_sort.sort(unsorted_list)
    assert unsorted_list == [-32, 2, 3, 3, 5, 76, 100, 444]


def test_empty():
    empty = []
    insertion_sort.sort(empty)
    assert empty == []
