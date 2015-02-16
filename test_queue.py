from queue import Queue
import pytest


tist = ('z', False, 1, None)


def test_init_queue():
    q = Queue()
    assert isinstance(q, Queue)


def test_enqueue():
    q = Queue()
    for data in tist:
        q.enqueue(data)
        assert q.list.head.data == data


def test_dequeue():
    q = Queue()
    for data in tist:
        q.enqueue(data)
    for data in tist:
        if q.list.head:
            assert q.dequeue() == 'z'
        else:
            with pytest.raises(LookupError) as context:
                q.dequeue()
                assert 'Empty Queue' in str(context.value)


def test_dequeue_empty():
    q = Queue()
    e_list = []
    for data in e_list:
        q.enqueue(data)
    for data in e_list:
        if q.list.head:
            assert q.dequeue() == 'z'
        else:
            with pytest.raises(LookupError) as context:
                q.dequeue()
                assert 'Empty Queue' in str(context.value)


def test_size():
    q = Queue()
    for data in range(4):
        q.enqueue(data)
    assert q.size() == 4


def test_display():
    q = Queue()
    for data in range(4):
        q.enqueue(data)
    assert q.display() == '(3, 2, 1, 0)'
