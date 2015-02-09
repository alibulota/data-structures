import linked_list as LL
import pytest
# import unittest


def test_init_Node():
    data = "test"
    head = LL.Node(data)
    assert type(head) == LL.Node
    assert head.data == data


def test_init_LinkedList():
    linked_list = LL.LinkedList()
    assert type(linked_list) == LL.LinkedList


def test_insert():
    linked_list = LL.LinkedList()
    data = "test"
    linked_list.insert(data)
    assert linked_list.head.data == data


def test_pop():
    linked_list = LL.LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    assert linked_list.pop() == 3


def test_size():
    linked_list = LL.LinkedList()
    assert linked_list.size() == 0
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    assert linked_list.size() == 3


def test_search():
    linked_list = LL.LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    find = linked_list.search(2)
    expected = (2)
    actual = (find)
    assert expected, actual


def test_remove():
    linked_list = LL.LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    node = linked_list.search(2)
    assert linked_list.remove(node) is not None
    assert linked_list.remove(node) == None


def test_display():
    linked_list = LL.LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    assert linked_list.display == "1, 2, 3"
