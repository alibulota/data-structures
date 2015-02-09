class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = 0
        self.size = 0

    def insert_node(self, data):
        inserted_node = Node(data)
        inserted_node.next = self.head
        self.head = inserted_node

    def pop_first_node(self):
        if self.head is not None:
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data
        else:
            raise ValueError
