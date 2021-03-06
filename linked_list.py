class Node(object):
    def __init__(self, data, next_node=None):
        self.data, self.next = data, next_node


class LinkedList(object):
    """Create and object-->linked_list."""
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        """Put the given value into Node at head of list."""
        inserted_node = Node(data)
        inserted_node.next = self.head
        self.head = inserted_node

    def pop(self):
        """Return node data, remove node from head of list."""
        value = self.head.data
        self.head = self.head.next
        return value

    def size(self):
        """Return length of linked list."""
        current_size = self.head
        list_size = 0
        while current_size is not None:
            list_size = list_size + 1
            current_size = current_size.next
        return list_size

    def search(self, data):
        find_node = self.head
        while find_node is not None:
            if find_node.data == data:
                return find_node
            else:
                find_node = find_node.next

    def remove(self, node):
        """Remove node from list"""
        prev_node = None
        cur_node = self.head
        while cur_node is not None:
            if cur_node == node:
                if prev_node is None:
                    self.head = node.next
                    return cur_node
                else:
                    prev_node.next = cur_node.next
                return cur_node
            else:
                cur_node = cur_node.next
        return None

    def display(self):
        """Print list in tuple literal format"""
        # source: http://dbader.org/blog/functional-linked-lists-in-python 
        def internal_display(node):
            if node is None:
                return ""
            elif node.next is None:
                return str(node.data)
            else:
                return str(node.data) + ", " + internal_display(node.next)
        return "(" + internal_display(self.head) + ")"
