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
            last_node = node
            data = last_node.data
            self.list.remove(last_node)
        else:
            raise LookupError('Empty Queue')
        return data

    def size(self):
        return self.list.size()

    def display(self):
        return self.list.display()
