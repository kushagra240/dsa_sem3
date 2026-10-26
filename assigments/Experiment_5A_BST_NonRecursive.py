# Input: n, followed by n integer keys (whitespace/newline separated).
# Output: Inorder and Preorder traversals, both non-recursive.

import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    cur = root
    while True:
        if key < cur.key:
            if cur.left is None:
                cur.left = Node(key)
                break
            cur = cur.left
        elif key > cur.key:
            if cur.right is None:
                cur.right = Node(key)
                break
            cur = cur.right
        else:
            break
    return root

def inorder_iterative(root):
    result, stack, cur = [], [], root
    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(str(cur.key))
        cur = cur.right
    return result

def preorder_iterative(root):
    if root is None:
        return []
    result, stack = [], [root]
    while stack:
        cur = stack.pop()
        result.append(str(cur.key))
        if cur.right is not None:
            stack.append(cur.right)
        if cur.left is not None:
            stack.append(cur.left)
    return result

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    values = data[1:1 + n]
    root = None
    for value in values:
        root = insert(root, value)
    print("Inorder:", " ".join(inorder_iterative(root)))
    print("Preorder:", " ".join(preorder_iterative(root)))

if __name__ == "__main__":
    main()
