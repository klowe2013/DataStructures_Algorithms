class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # If there is no list
        if self.head is None:
            print('No items to pop')
        # If there is only one item in the list
        elif self.head.next is None:
            self.head = None
            self.tail = None
        # Normal behavior
        else:
            pre = self.head
            temp = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            self.length -= 1

    def get(self, index):
        if (index >= self.length) or (index < 0):
            return None

        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        return tmp

    def set_value(self, index, value):
        if (index >= self.length) or (index < 0):
            return None

        tmp = self.get(index)
        if tmp:
            tmp.value = value
            return True
        return False

    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        # Get current index-1th element
        tmp = self.get(index-1)
        # Create new Node
        new_node = Node(value)
        # Point new node's next to tmp's next
        new_node.next = tmp.next
        # Point the left part of the list to the new node
        tmp.next = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == (self.length-1):
            return self.pop()
        pre = self.get(index-1)
        rem = pre.next
        pre.next = rem.next
        rem.next = None
        self.length -= 1
        return rem

    def reverse(self):
        # Start at the head
        tmp = self.head
        self.head = self.tail
        self.tail = tmp

        prev = None
        for _ in range(self.length):
            # while tmp.next:
            next = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = next
            # if tmp.next:
            #     next = tmp.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()
