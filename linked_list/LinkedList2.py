class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        list_vals = []
        while temp is not None:
            list_vals.append(temp.value)
            temp = temp.next
        print(list_vals)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True

        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1
        return True

    def pop(self):
        # If there is no list, return None
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
            self.tail = None
            return True
        # Remove from end. Need to get the value that points to tail
        # Tail is identified where next is None
        # So the value that points to tail is tmp.next.next is None
        tmp = self.head
        while tmp.next.next is not None:
            tmp = tmp.next
        self.tail = tmp
        self.length -= 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        # If there is no list, there is nothing to append to
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return True
        # Add to beginning. Create new node, point it's next to self.head, then change head to new node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        # If there is no list return None
        if self.head is None:
            return True
        # If there is only one element
        elif self.head.next is None:
            self.head = None
            self.tail = None
            return True
        # Remove from beginning. Get tmp as second element (head.next),
        # remove pointer from old head, and reset head to tmp
        tmp = self.head.next
        self.head.next = None
        self.head = tmp
        self.length -= 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        tmp = self.head
        # Step until index
        for _ in range(index):
            tmp = tmp.next
        return tmp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None

        # Get this node
        this_node = self.get(index)
        this_node.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)

        # Get index - 1 so that it can point to the new node at index
        tmp = self.get(index-1)
        new_node = Node(value)
        new_node.next = tmp.next
        # Now set tmp's next to the new node
        tmp.next = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()

        # Get the item before the removed index
        prev = self.get(index-1)
        # The removed item is prev.next
        rem = prev.next
        # Set prev.next pointer to rem.next
        prev.next = rem.next
        rem.next = None

        self.length -= 1
        return True

    def reverse(self):
        # Reversing is the classic tricky one

        # Reverse head and tail
        tmp = self.head
        self.head = self.tail
        self.tail = tmp

        # tmp is the previous head and points to the next element. Let's also start prev as None
        prev = None
        # We'll need to loop through the list
        for _ in range(self.length):
            # Get pointer for next
            next = tmp.next
            # Point tmp.next to prev
            tmp.next = prev
            # Now scoot the pointers
            prev = tmp
            tmp = next
        return True


ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.pop()
ll.append(4)
ll.prepend(6)
ll.prepend(5)
ll.insert(2, 7)
ll.print_list()
ll.reverse()
ll.print_list()
