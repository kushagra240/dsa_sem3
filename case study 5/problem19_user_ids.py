"""Case Study 5: Social networking application user IDs in BST."""

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
        result = []
        if node.left is not None:
            result.extend(self.inorder_recursive(node.left))
        result.append(node.value)
        if node.right is not None:
            result.extend(self.inorder_recursive(node.right))
        return result

    def preorder_recursive(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        result = [node.value]
        if node.left is not None:
            result.extend(self.preorder_recursive(node.left))
        if node.right is not None:
            result.extend(self.preorder_recursive(node.right))
        return result

    def postorder_recursive(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        result = []
        if node.left is not None:
            result.extend(self.postorder_recursive(node.left))
        if node.right is not None:
            result.extend(self.postorder_recursive(node.right))
        result.append(node.value)
        return result

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
    r_in = tree.inorder_recursive()
    r_pre = tree.preorder_recursive()
    r_post = tree.postorder_recursive()
    i_in = tree.inorder_iterative()
    i_pre = tree.preorder_iterative()
    i_post = tree.postorder_iterative()
    print(f"Social networking application user IDs in BST -> Recursive Inorder: {r_in}")
    print(f"Social networking application user IDs in BST -> Recursive Preorder: {r_pre}")
    print(f"Social networking application user IDs in BST -> Recursive Postorder: {r_post}")
    print(f"Social networking application user IDs in BST -> Non-Recursive Inorder: {i_in}")
    print(f"Social networking application user IDs in BST -> Non-Recursive Preorder: {i_pre}")
    print(f"Social networking application user IDs in BST -> Non-Recursive Postorder: {i_post}")
    print(f"Social networking application user IDs in BST -> Results match: {r_in == i_in and r_pre == i_pre and r_post == i_post}")



if __name__ == "__main__":
    main()
