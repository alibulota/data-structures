import linked_list as ll


class Stack(object):

    def __init__(self):
        self.linked_list = ll.LinkedList()

    def push(self, data):
        self.linked_list.insert(data)

    def pop(self):
        value = self.linked_list.pop()
        return value
