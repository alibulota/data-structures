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
