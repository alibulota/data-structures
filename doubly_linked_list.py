# http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/


class Node(object):
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        """Insert data to at head"""
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        elif self.head is not None:
            node.prev = self.head
            self.head.prev = node
            self.head = node

    def append(self, data):
        """Insert data to at head"""
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        elif self.head is not None:
            node.next = self.tail
            self.tail.next = node
            self.tail = node

    def pop(self):
        """Remove and return head value"""
        if self.head is not None:
            value = self.head.data
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
        return value

    def shift(self):
        """Remove and return tail value"""
        if self.tail is not None:
            value = self.tail.data
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
        return value

    def remove(self, data):
        """Remove first instance of val"""
        if self.head is None:
            raise LookupError('Data not in list.')
        elif self.head.data == data:
            self.head = self.head.next
        elif self.tail.data == data:
            self.tail = self.tail.prev
        else:
            curr_node = self.head
            while True:
                if curr_node.data == data:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                    break
                else:
                    if curr_node.next is None:
                        raise LookupError('Data not in list.')
                    else:
                        curr_node = curr_node.next
