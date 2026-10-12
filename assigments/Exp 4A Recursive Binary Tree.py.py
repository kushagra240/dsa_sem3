from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    data: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def create_tree(position: str = "root") -> Optional[Node]:
    value = input(f"Enter {position} category/book (or NULL for no node): ").strip()
    if value.upper() == "NULL":
        return None

    node = Node(value)
    node.left = create_tree(f"left child of '{value}'")
    node.right = create_tree(f"right child of '{value}'")
    return node


def inorder(root: Optional[Node]) -> None:
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def preorder(root: Optional[Node]) -> None:
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root: Optional[Node]) -> None:
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


def main() -> None:
    print("=== Department of CSE - DSA Lab ===")
    print("Assignment 4: Binary Tree and Recursive Traversals")
    print("\nCreate Library Catalog Binary Tree")
    root = create_tree()

    if root is None:
        print("\nThe catalog is empty.")
        return

    print("\nBook Categories (Inorder Traversal):")
    inorder(root)
    print()

    print("Catalog Structure (Preorder Traversal):")
    preorder(root)
    print()

    print("Archive/Delete Order (Postorder Traversal):")
    postorder(root)
    print()


if __name__ == "__main__":
    main()
