class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    newnode = Node(data)

    if root is None:
        return newnode

    curr = root

    while True:
        if data < curr.data:
            if curr.left is None:
                curr.left = newnode
                break
            curr = curr.left

        else:
            if curr.right is None:
                curr.right = newnode
                break
            curr = curr.right

    return root


def inorder(root):
    stack = []
    curr = root

    while stack or curr is not None:

        while curr is not None:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        print(curr.data)

        curr = curr.right


def preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        curr = stack.pop()
        print(curr.data)

        if curr.right is not None:
            stack.append(curr.right)

        if curr.left is not None:
            stack.append(curr.left)


root = None

n = int(input())

for i in range(n):
    data = int(input())
    root = insert(root, data)

print("Inorder:")
inorder(root)

print("-------------------------------------")

print("Preorder:")
preorder(root)

print("-------------------------------------")