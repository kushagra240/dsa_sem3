"""Binary Tree Recursive Traversal.

This program creates a binary tree dynamically from user input,
then displays its preorder traversal using recursive logic.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def preorder(temp):
    if temp is not None:
        print(temp.data, end=" ")
        preorder(temp.left)
        preorder(temp.right)


def inorder(temp):
    if temp is not None:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right)


def postorder(temp):
    if temp is not None:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.data, end=" ")


def main():
    print("Binary Tree Recursive Traversal Demo")
    print("=" * 35)
    root = create()

    print("\nPreorder Traversal:")
    preorder(root)

    print("\n\nInorder Traversal:")
    inorder(root)

    print("\n\nPostorder Traversal:")
    postorder(root)


if __name__ == "__main__":
    main()
