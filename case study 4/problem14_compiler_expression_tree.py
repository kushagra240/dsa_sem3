"""Case Study 4: Compiler Expression Tree."""

from __future__ import annotations


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, values=None):
        self.root = None
        if values:
            for value in values:
                self.insert(value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = Node(value)
                return
            queue.append(node.left)
            if node.right is None:
                node.right = Node(value)
                return
            queue.append(node.right)

    def recursive_inorder(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        return self.recursive_inorder(node.left) + [node.value] + self.recursive_inorder(node.right)

    def recursive_preorder(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        return [node.value] + self.recursive_preorder(node.left) + self.recursive_preorder(node.right)

    def recursive_postorder(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        return self.recursive_postorder(node.left) + self.recursive_postorder(node.right) + [node.value]

    def iterative_inorder(self):
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

    def iterative_preorder(self):
        if self.root is None:
            return []
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result

    def iterative_postorder_two_stacks(self):
        if self.root is None:
            return []
        stack1 = [self.root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)
        result = []
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
    tree = BinaryTree(values)
    print(f"Compiler Expression Tree -> Non-Recursive Postorder Traversal: {tree.iterative_postorder_two_stacks()}")



if __name__ == "__main__":
    main()
