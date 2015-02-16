from stack import Stack
import pytest


class StackTest():

    def test_init(self):
        stack = Stack()
        assert stack is not None

    def test_push():
        stack = Stack()
        stack.push(3)
        stack.push(2)
        stack.push(1)
        assert stack.pop() == 1
        assert stack.pop() == 2
        assert stack.pop() == 3

    def test_pop():
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
