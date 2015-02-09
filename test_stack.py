import stack as st
import sys
import pytest


class StackTest():

    def test_init(self):
        stack = st.Stack()
        assert type(stack) == st.Stack

    def test_push(self):
        self.assertEqual(self.append.data)

    def test_pop(self):
        self.asserEqual(self.pop.data)
        self.assertEqual(self.length == 0)
