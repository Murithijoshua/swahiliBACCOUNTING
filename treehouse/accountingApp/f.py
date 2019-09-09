class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                data > self.data:
                if self.right is None:
                    self.left = Node(data)
                elseclass
                Node:


def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data


def insert(self, data):
    # Compare the new value with the parent node
    if self.data:
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    else:
        self.data = data


# Print the tree
def PrintTree(self):
    if self.left:
        self.left.PrintTree()
    print(self.data),
    if self.right:
        self.right.PrintTree()


# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree():
self.right.insert(data)
else:
self.data = data


def printTree(self):
    if self.left:
        self.left.printTree()
    print(self.data)
    if self.right:
        self.right.PrintTree()
    print(self.data)


root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)

root.printTree()

