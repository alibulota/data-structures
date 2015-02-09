from linked_list import LinkedList
import sys
import unittest
import pytest


LinkedList = ("1, 2, 3")


def test_init():
    test_list = LinkedList
    new_node = test_list.data
    expected = (new_node)
    actual = (new_node)
    assert (expected, actual)


def test_insert_node():
    test_list = LinkedList
    test_list.insert_node(100)
    expected = (100, None)
    actual = (test_list.head.data, test_list.head)
    assert expected, actual


def test_pop_first_node():
    test_list = LinkedList
    pop_test = (test_list.pop_first_node)
    expected = (2, 3)
    actual = (pop_test, test_list.head)
    assert expected, actual


def test_size_list():
    test_list = LinkedList
    expected = 3
    actual = test_list.size_list
    assert expected, actual


def test_search_node():
    test_list = LinkedList
    found_node = test_list.search_node(3)
    expected = (3)
    actual = (found_node)
    assert expected, actual


def test_remove_node():
    test_list = LinkedList
    test_list = test_list.remove_node(1)
    expected = (1)
    actual = (test_list)
    assert expected, actual


def test_print_list():
    test_list = LinkedList
    test_list = test_list.print_list()
    expected = (1, 2, 3)
    actual = (test_list)
    assert expected, actual
