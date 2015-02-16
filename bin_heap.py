# http://interactivepython.org/courselib/static/pythonds/Trees/heap.html


class binHeap(object):
    def __init__(self):
        self.heap = [0]
        self.curr_size = 0

    def push(self, value):
        self.heap.append(value)
        self.curr_size = self.curr_size += 1
        self.up(self.curr_size)

    def up(self, value):
        while value // 2 > 0:
            if self.heap[value // 2]:
                trade = self.heap[value // 2]
                self.heap[value // 2] = self.heap[value]
                self.heap[value] = trade
            value = value // 2

    def pop(self):
        r_value = self.heap[1]
        self.heap[1] = self.heap[self.curr_size]
        self.curr_size = self.curr_size -1
        self.heap.pop()
        self.down(1)
        return r_value

    def down(self, value):
        while (value * 2) <= self.curr_size:
            mini_child = self.mini_child(value)
            if self.heap[value] > self.heap[mini_child]:
                trade = self.heap[value]
                self.heap[value] = self.heap[mini_child]
                self.heap[mini_child] = trade
            value = mini_child

    def mini_child(self, value):
        if value * 2 +1 > self.curr_size:
            return value * 2
        else:
            if self.heap[value*2] < self.heap[value*2+1]:
                return value * 2
            else:
                return value * 2 + 1

    def heapify(self, hlist):
        h = len(hlist) // 2
        self.curr_size = len(hlist)
        self.heap = [0] + hlist[:]
        while (h > 0):
            self.down(h)
            h = h - 1