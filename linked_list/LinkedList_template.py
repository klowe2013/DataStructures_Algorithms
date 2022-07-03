class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        pass

    def pop(self):
        pass

    def prepend(self, value):
        pass

    def pop_first(self):
        pass

    def get(self, index):
        pass

    def set_value(self, index, value):
        pass

    def insert(self, index, value):
        pass

    def remove(self, index):
        pass

    def reverse(self):
        pass
