import bin_heap as bh

class pQueue(object):
    def __init__(self):
        self.bin_heap = bh.binHeap()


    def insert(self, input_value, order):
        self.bin_heap.push(input_value)


    def pop(self):
        input_value = self.bin_heap.pop()
        return input_value


    def peek(self, input_value):
        input_value = self.bin_heap.pop()
        return input_value
