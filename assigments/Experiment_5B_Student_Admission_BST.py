# Student Admission Record Management
# Input: n, followed by n admission IDs (integers).
# The admission ID is the BST key. Traversals are non-recursive.

import sys

class Node:
    def __init__(self, admission_id):
        self.admission_id = admission_id
        self.left = None
        self.right = None

def insert(root, admission_id):
    if root is None:
        return Node(admission_id)
    current = root
    while True:
        if admission_id < current.admission_id:
            if current.left is None:
                current.left = Node(admission_id)
                return root
            current = current.left
        elif admission_id > current.admission_id:
            if current.right is None:
                current.right = Node(admission_id)
                return root
            current = current.right
        else:
            return root

def inorder(root):
    answer, stack, current = [], [], root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        answer.append(str(current.admission_id))
        current = current.right
    return answer

def preorder(root):
    if root is None:
        return []
    answer, stack = [], [root]
    while stack:
        current = stack.pop()
        answer.append(str(current.admission_id))
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return answer

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    root = None
    for admission_id in data[1:1 + n]:
        root = insert(root, admission_id)
    print("Inorder:", " ".join(inorder(root)))
    print("Preorder:", " ".join(preorder(root)))

if __name__ == "__main__":
    main()
