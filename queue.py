from linked_list import LinkedList

class Queue(object):
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, data):
        self.list.insert(data)

    def dequeue(self):
        if self.list.head:
            node = self.list.head
            while node.next:
                node = node.next
            prev_node = node
            data = prev_node.data
            self.list.remove(prev_node)
        else:
            raise LookupError('Empty Queue')
        return data

    def size(self):
        return self.list.size()

    def display(self):
        return self.list.display()