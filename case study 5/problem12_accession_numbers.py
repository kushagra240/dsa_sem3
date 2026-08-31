"""Case Study 5: Library accession numbers in BST."""

from __future__ import annotations


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, values=None):
        self.root = None
        if values:
            for value in values:
                self.insert(value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
            else:
                return

    def inorder_recursive(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        return self.inorder_recursive(node.left) + [node.value] + self.inorder_recursive(node.right)

    def preorder_recursive(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        return [node.value] + self.preorder_recursive(node.left) + self.preorder_recursive(node.right)

    def postorder_recursive(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        return self.postorder_recursive(node.left) + self.postorder_recursive(node.right) + [node.value]

    def inorder_iterative(self):
        result = []
        stack = []
        current = self.root
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def preorder_iterative(self):
        if self.root is None:
            return []
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result

    def postorder_iterative(self):
        if self.root is None:
            return []
        result = []
        stack1 = [self.root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            result.append(node.value)
        return result


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError('Stack is empty')
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0



def main():

    values = [50, 30, 70, 20, 40, 60, 80]
    tree = BST(values)
    r_in = tree.recursive_inorder() if hasattr(tree, 'recursive_inorder') else tree.inorder_recursive()
    r_pre = tree.recursive_preorder() if hasattr(tree, 'recursive_preorder') else tree.preorder_recursive()
    r_post = tree.recursive_postorder() if hasattr(tree, 'recursive_postorder') else tree.postorder_recursive()
    i_in = tree.iterative_inorder() if hasattr(tree, 'iterative_inorder') else tree.inorder_iterative()
    i_pre = tree.iterative_preorder() if hasattr(tree, 'iterative_preorder') else tree.preorder_iterative()
    i_post = tree.iterative_postorder_two_stacks() if hasattr(tree, 'iterative_postorder_two_stacks') else tree.postorder_iterative()
    print(f"Library accession numbers in BST -> Recursive Inorder: {r_in}")
    print(f"Library accession numbers in BST -> Recursive Preorder: {r_pre}")
    print(f"Library accession numbers in BST -> Recursive Postorder: {r_post}")
    print(f"Library accession numbers in BST -> Non-Recursive Inorder: {i_in}")
    print(f"Library accession numbers in BST -> Non-Recursive Preorder: {i_pre}")
    print(f"Library accession numbers in BST -> Non-Recursive Postorder: {i_post}")



if __name__ == "__main__":
    main()
