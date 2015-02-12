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
            with pytest.raises(LookupError):
                q.dequeue()


def test_size():
    q = Queue()
    return q.list.size() == 4



def test_display():
    q = Queue()
    return q.list.display() == tist