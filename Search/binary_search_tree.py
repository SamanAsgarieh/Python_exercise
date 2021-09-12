class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if (value < self.value):
            if (self.left is None):
                self.left = BinarySearchTree(value, self.depth + 1)
                print(
                    f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if (self.right is None):
                self.right = BinarySearchTree(value, self.depth + 1)
                print(
                    f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    # Define .get_node_by_value() below:
    def get_node_by_value(self, value):
        if value == self.value:
            return self
        elif value < self.value and self.left:
            return self.left.get_node_by_value(value)
        elif value > self.value and self.right:
            return self.right.get_node_by_value(value)
        else:
            return None

    def depth_first_traversal(self):
        if (self.left is not None):
            self.left.depth_first_traversal()
        print(f'Depth={self.depth}, Value={self.value}')
        if (self.right is not None):
            self.right.depth_first_traversal()


root = BinarySearchTree(100)

root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)

# Get nodes by value below:
print(root.get_node_by_value(75).value)
print(root.get_node_by_value(55))

print("Creating Binary Search Tree rooted at value 15:")


print("Printing the inorder depth-first traversal:")
root.depth_first_traversal()
