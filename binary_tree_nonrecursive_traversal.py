"""Non-Recursive Preorder and Inorder Traversal in Binary Tree.

This program creates a binary tree dynamically from user input and
prints the preorder and inorder traversal without using recursion.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Stack:
    def __init__(self, size=100):
        self.TOP = -1
        self.st = [None] * size

    def push(self, item):
        if self.TOP == len(self.st) - 1:
            print("Stack Overflow")
            return False
        self.TOP += 1
        self.st[self.TOP] = item
        return True

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return None
        item = self.st[self.TOP]
        self.TOP -= 1
        return item

    def is_empty(self):
        return self.TOP == -1


def create():
    x = int(input("Enter the data (-1 for no node): "))

    if x == -1:
        return None

    root = Node(x)

    print(f"Enter left child of {x}")
    root.left = create()

    print(f"Enter right child of {x}")
    root.right = create()

    return root


def preorder_non_recursive(root):
    if root is None:
        print("Tree is empty")
        return

    s = Stack()
    current = root

    while current is not None or not s.is_empty():
        while current is not None:
            print(current.data, end=" ")
            s.push(current)
            current = current.left

        if not s.is_empty():
            current = s.pop()
            current = current.right

    print()


def inorder_non_recursive(root):
    if root is None:
        print("Tree is empty")
        return

    s = Stack()
    current = root

    while current is not None or not s.is_empty():
        while current is not None:
            s.push(current)
            current = current.left

        if not s.is_empty():
            current = s.pop()
            print(current.data, end=" ")
            current = current.right

    print()


def main():
    print("Binary Tree Non-Recursive Traversal Demo")
    print("=" * 40)
    root = create()

    print("\nPreorder Traversal (Non-Recursive):")
    preorder_non_recursive(root)

    print("Inorder Traversal (Non-Recursive):")
    inorder_non_recursive(root)


if __name__ == "__main__":
    main()
