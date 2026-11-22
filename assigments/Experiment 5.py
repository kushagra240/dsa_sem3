class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        curr = self.root
        while True:
            if data < curr.data:
                if curr.left is None:
                    curr.left = Node(data)
                    return
                curr = curr.left
            elif data > curr.data:
                if curr.right is None:
                    curr.right = Node(data)
                    return
                curr = curr.right
            else:
                print(f"Duplicate value {data} ignored.")
                return

    def inorder_non_recursive(self):
        result = []
        stack = []
        curr = self.root
        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.data)
            curr = curr.right
        return result

    def preorder_non_recursive(self):
        result = []
        if self.root is None:
            return result
        stack = [self.root]
        while stack:
            curr = stack.pop()
            result.append(curr.data)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return result


def main():
    tree = BST()
    n = int(input("Enter number of nodes: "))
    if n < 0:
        print("Number of nodes cannot be negative.")
        return
    for i in range(n):
        data = int(input(f"Enter value {i + 1}: "))
        tree.insert(data)
    print("\nInorder Traversal (Non-Recursive):")
    print(*tree.inorder_non_recursive())
    print("\nPreorder Traversal (Non-Recursive):")
    print(*tree.preorder_non_recursive())


if __name__ == "__main__":
    main()