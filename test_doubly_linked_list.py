from doubly_linked_list import DoublyList, Node
import pytest


tist = ('a', 100, False, None, 'Butters')


def test_init_Node():
    for data in tist:
        node = Node(data)
        assert isinstance(node, Node)
        assert node.data == data


def test_init_DoublyList():
    for data in tist:
        node = Node(data)
        assert isinstance(node, Node)
        assert node.data == data


def test_insert():
    doubly_linked_list = DoublyList()
    for data in tist:
        doubly_linked_list.insert(data)
        assert doubly_linked_list.head.data == data
    assert doubly_linked_list.head.data == tist [-1]


def test_append():
    doubly_linked_list = DoublyList()
    for data in tist:
        doubly_linked_list.append(data)
        assert doubly_linked_list.tail.data == data
    assert doubly_linked_list.tail.data == tist [-1]


def test_pop():
    doubly_linked_list = DoublyList()
    for data in tist:
        doubly_linked_list.append(data)
    for data in tist:
        assert doubly_linked_list.pop() == data
    assert doubly_linked_list.pop() is None



def test_shift():
    doubly_linked_list = DoublyList()
    for data in tist:
        doubly_linked_list.insert(data)
    for data in tist:
        assert doubly_linked_list.shift() == data
    assert doubly_linked_list.shift() is None


def test_remove():
    doubly_linked_list = DoublyList()
    for data in tist:
        assert doubly_linked_list.remove(100) == 100
        # else:
        #     with pytest.raises(LookupError)as context:
        #         remove()
        #         assert "Data not in list" in str(context.value)