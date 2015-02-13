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
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                if curr_node == node:
                    if prev_node is None:
                        self.head = node.next
                    return curr_node
                else:
                    prev_node.next = curr_node.next
                return curr_node
            else:
                curr_node = curr_node.next
            raise LookupError("Data not in list.")



    #     def search(self, data):
    #     find_node = self.head
    #     while find_node is not None:
    #         if find_node.data == data:
    #             return find_node
    #         else:
    #             find_node = find_node.next
    #
    # def remove(self, node):
    #     """Remove node from list"""
    #     prev_node = None
    #     cur_node = self.head
    #     while cur_node is not None:
    #         if cur_node == node:
    #             if prev_node is None:
    #                 self.head = node.next
    #                 return cur_node
    #             else:
    #                 prev_node.next = cur_node.next
    #             return cur_node
    #         else:
    #             cur_node = cur_node.next
    #     return None