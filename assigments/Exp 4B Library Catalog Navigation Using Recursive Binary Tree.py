class Book:
    def __init__(self,book):
        self.book=book
        self.left=None
        self.right=None

def create():
    x=input("Enter book (0 to stop):")
    if x=="0":
        return None

    root=Book(x)        #object creation

    print(f"Enter left of {x}:")
    root.left=create()
    print(f"Enter right of {x}:")
    root.right=create()
    return root

def preorder(root):
    if root is not None:
        print(root.book)           
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        preorder(root.left)
        print(root.book) 
        preorder(root.right)

def postorder(root):
    if root is not None:
        preorder(root.left)
        preorder(root.right)
        print(root.book)

root=create()
print("Preorder:")
preorder(root)
print("-------------------------------------")
print("Inorder:")
inorder(root)
print("-------------------------------------")
print("Postorder:")
postorder(root)
print("-------------------------------------")