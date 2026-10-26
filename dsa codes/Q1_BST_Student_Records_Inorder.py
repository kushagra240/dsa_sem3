class Node:
    def __init__(self, roll, attendance):
        self.roll = roll
        self.attendance = attendance
        self.left = None
        self.right = None


def insert(root, roll, attendance):
    if root is None:
        return Node(roll, attendance)

    if roll < root.roll:
        root.left = insert(root.left, roll, attendance)
    else:
        root.right = insert(root.right, roll, attendance)

    return root


def inorder(root):
    stack = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.roll, current.attendance)
        current = current.right


n = int(input())
root = None

for i in range(n):
    roll, attendance = input().split()
    root = insert(root, int(roll), float(attendance))

inorder(root)
