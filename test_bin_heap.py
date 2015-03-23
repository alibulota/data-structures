from bin_heap import binHeap
import pytest
import random


def test_empty_heap():
    blist = binHeap()
    assert blist.heap == [0]


def test_push_pop():
    blist = binHeap()
    blist.push(123)
    assert blist.pop() == 123


def all_list(heap):
    value_input = []
    while True:
        try:
            value_input.append(heap.pop())
        except IndexError:
            return value_input
    return value_input


def test_input_random():
    blist = binHeap()
    for x in random.sample(range(123), 123):
        blist.push(x)
    assert all_list(blist) == range(0, 123)
