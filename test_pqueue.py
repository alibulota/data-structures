from pqueue import pQueue


def test_insert(self):
    pq = pQueue()
    pq.insert(5, 3)
    assert pq.insert() == 5


def test_pop(self):
    pq = pQueue()
    pq.insert("hello", 10)
    pq.insert("butts", 99)
    pq.insert("puppies", 1)
    assert pq.pop() == "puppies"
    assert pq.pop() == "hello"
    assert pq.pop() == "butts"
    assert curr_size == 0

def test_peek(self):
    pq = pQueue()
    pq.insert("hello", 2)
    pq.insert("butts", 3)
    pq.insert("puppies", 1)
    assert pq.peek() == "puppies"


