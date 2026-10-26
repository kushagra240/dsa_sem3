# Employee Database Analysis
# Input: n, n employee IDs, then one new employee ID.
# Employee IDs form the BST keys.

import sys
from collections import deque

class Node:
    def __init__(self, employee_id):
        self.employee_id = employee_id
        self.left = None
        self.right = None

def insert(root, employee_id):
    if root is None:
        return Node(employee_id)
    node = root
    while True:
        if employee_id < node.employee_id:
            if node.left is None:
                node.left = Node(employee_id)
                return root
            node = node.left
        elif employee_id > node.employee_id:
            if node.right is None:
                node.right = Node(employee_id)
                return root
            node = node.right
        else:
            return root

def level_order(root):
    if root is None:
        return []
    output, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(str(node.employee_id))
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        output.append(level)
    return output

def leaf_ids(root):
    if root is None:
        return []
    output, stack = [], [root]
    while stack:
        node = stack.pop()
        if node.left is None and node.right is None:
            output.append(str(node.employee_id))
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return output

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    ids = data[1:1 + n]
    if len(data) < n + 2:
        return
    new_id = data[n + 1]
    root = None
    for employee_id in ids:
        root = insert(root, employee_id)

    print("Original tree level-wise:")
    for i, level in enumerate(level_order(root), 1):
        print("Level", i, ":", " ".join(level))

    root = insert(root, new_id)
    print("New tree level-wise:")
    for i, level in enumerate(level_order(root), 1):
        print("Level", i, ":", " ".join(level))

    print("Height:", len(level_order(root)))
    print("Leaf nodes:", " ".join(leaf_ids(root)))

if __name__ == "__main__":
    main()
