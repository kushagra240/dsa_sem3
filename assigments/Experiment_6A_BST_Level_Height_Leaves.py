# Input: n, n integer keys, then one new key to insert.
# Prints the BST level-wise before and after insertion, height in levels,
# and leaf nodes of the updated tree.

import sys
from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    current = root
    while True:
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
                break
            current = current.left
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
                break
            current = current.right
        else:
            break
    return root

def levels(root):
    if root is None:
        return []
    result, queue = [], deque([root])
    while queue:
        level_values = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level_values.append(str(node.key))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_values)
    return result

def leaves(root):
    if root is None:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        if node.left is None and node.right is None:
            result.append(str(node.key))
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    values = data[1:1 + n]
    if len(data) < n + 2:
        return
    new_key = data[n + 1]
    root = None
    for key in values:
        root = insert(root, key)

    print("Original tree level-wise:")
    for i, level in enumerate(levels(root), 1):
        print("Level", i, ":", " ".join(level))

    root = insert(root, new_key)
    print("New tree level-wise:")
    for i, level in enumerate(levels(root), 1):
        print("Level", i, ":", " ".join(level))

    current_levels = levels(root)
    print("Height:", len(current_levels))
    print("Leaf nodes:", " ".join(leaves(root)))

if __name__ == "__main__":
    main()
