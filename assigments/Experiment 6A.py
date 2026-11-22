from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        curr = self.root
        while True:
            if data < curr.data:
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left
            elif data > curr.data:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right
            else:
                print(f"Duplicate value {data} ignored.")
                return

    def level_order(self, label):
        print(label)
        if not self.root:
            print("Tree is empty.")
            return
        q = deque([self.root])
        level = 0
        while q:
            values = []
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                values.append(str(curr.data))
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            print(f"Level {level}: " + " ".join(values))
            level += 1

    def height(self, node):
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def get_leaves(self, node):
        result = []
        if not node:
            return result
        if not node.left and not node.right:
            return [node.data]
        result.extend(self.get_leaves(node.left))
        result.extend(self.get_leaves(node.right))
        return result


def main():
    orig_tree = BST()
    new_tree = BST()
    n = int(input("Enter number of nodes: "))
    if n < 0:
        print("Number of nodes cannot be negative.")
        return
    values = []
    for i in range(n):
        val = int(input(f"Enter value {i + 1}: "))
        values.append(val)
        orig_tree.insert(val)

    for val in values:
        new_tree.insert(val)

    orig_tree.level_order("\nOriginal BST - Level-wise:")
    new_tree.level_order("\nNew BST - Level-wise:")
    print("\nHeight of Original BST (in edges):", orig_tree.height(orig_tree.root))
    leaves = orig_tree.get_leaves(orig_tree.root)
    print("Leaf Nodes of Original BST: " + " ".join(map(str, leaves)))


if __name__ == "__main__":
    main()