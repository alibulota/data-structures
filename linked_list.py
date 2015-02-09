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

    def size_list(self):
        current_size = self.head
        size_count = 0
        while current_size is not None:
            size_count = size_count + 1
            current_size = current_size.next
        print size_count
        return size_count

    def search_node(self, data):
        traverse = self.head
        found = False
        while traverse is not None and not found:
            if traverse.data == data:
                found = True
                print traverse.data
                return traverse
            else:
                traverse = traverse.next

    def remove_node(self, data):
        takeout = self.head
        found = False
        while takeout is not None and not found:
            if takeout.data == data:
                takeout == takeout.next.next
                found = True
                print takeout.data
                return data
