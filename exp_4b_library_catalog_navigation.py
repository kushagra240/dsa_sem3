"""Exp 4B: Library Catalog Navigation."""


class BookNode:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, book_id, title):
        new_node = BookNode(book_id, title)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if book_id < current.book_id:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif book_id > current.book_id:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                print(f"Book ID {book_id} already exists in the catalog.")
                return

    def inorder_recursive(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []

        result = []
        if node.left is not None:
            result.extend(self.inorder_recursive(node.left))
        result.append((node.book_id, node.title))
        if node.right is not None:
            result.extend(self.inorder_recursive(node.right))
        return result

    def preorder_recursive(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []

        result = [(node.book_id, node.title)]
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
        result.append((node.book_id, node.title))
        return result


def display_sequence(label, records):
    print(f"{label}: ")
    if not records:
        print("  No books found.")
        return
    for book_id, title in records:
        print(f"  {book_id} -> {title}")


def main():
    catalog = BinaryTree()

    books = [
        (104, "Data Structures"),
        (201, "Operating Systems"),
        (50, "Database Management"),
        (78, "Computer Networks"),
        (150, "Artificial Intelligence"),
        (25, "Discrete Mathematics"),
        (60, "Software Engineering"),
        (110, "Compiler Design"),
        (300, "Web Technologies"),
    ]

    for book_id, title in books:
        catalog.insert(book_id, title)

    print("Library Catalog Navigation")
    print("=" * 40)

    inorder_records = catalog.inorder_recursive()
    preorder_records = catalog.preorder_recursive()
    postorder_records = catalog.postorder_recursive()

    display_sequence("Inorder Traversal", inorder_records)
    display_sequence("Preorder Traversal", preorder_records)
    display_sequence("Postorder Traversal", postorder_records)


if __name__ == "__main__":
    main()
