class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def print_tree(self):
        pass

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        tmp = self.root

        while True:
            if value < tmp.value:
                # If there is no left, place the node
                if tmp.left is None:
                    tmp.left = new_node
                    return True
                # Else move left
                tmp = tmp.left
            elif value > tmp.value:
                if tmp.right is None:
                    tmp.right = new_node
                    return True
                # Else move right
                tmp = tmp.right
            else:
                return False

    def contains(self, value):
        tmp = self.root
        while tmp is not None:
            if value < tmp.value:
                tmp = tmp.left
            elif value > tmp.value:
                tmp = tmp.right
            else:
                return True
        return False

    def remove(self, value):
        pass


bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(6)
bst.insert(8)

print(bst.contains(9))
