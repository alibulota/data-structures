import random
from quick_sort import quick_sort


def test_quick_sort():
    list_1 = [0, 1, 2, 3, 4, 5]
    list_2 = list(list_1)
    list_2.reverse()
    expected = list(list_1)
    assert quick_sort(list_1) == expected
    assert quick_sort(list_2) == expected
    #  These should come out to be the same


def test_quick_sort_2():
    list_1 = [random.randrange(100000) for i in xrange(500)]
    expected = list(list_1)
    expected.sort()
    assert quick_sort(list_1) == expected


def test_quick_sort_3():
    list_1 = [3 for i in xrange(50)]
    expected = list(list_1)
    assert quick_sort(list_1) == expected
