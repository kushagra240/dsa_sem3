class Student:
    def __init__(self, admission_no):
        self.admission_no = admission_no
        self.left = None
        self.right = None


def insert(root, admission_no):
    newnode = Student(admission_no)

    if root is None:
        return newnode

    curr = root

    while True:
        if admission_no < curr.admission_no:
            if curr.left is None:
                curr.left = newnode
                break
            curr = curr.left

        else:
            if curr.right is None:
                curr.right = newnode
                break
            curr = curr.right

    return root


def inorder(root):
    stack = []
    curr = root

    while stack or curr is not None:

        while curr is not None:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        print(curr.admission_no)

        curr = curr.right


def preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        curr = stack.pop()
        print(curr.admission_no)

        if curr.right is not None:
            stack.append(curr.right)

        if curr.left is not None:
            stack.append(curr.left)


root = None

n = int(input())

for i in range(n):
    admission_no = int(input())
    root = insert(root, admission_no)

print("Inorder:")
inorder(root)

print("-------------------------------------")

print("Preorder:")
preorder(root)

print("-------------------------------------")