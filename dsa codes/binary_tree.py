#create binary tree and perform inorder, preorder and postorder traversals.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def create(self):
        val=input("Enter the value for node:")
        if val=="":
            return None
        root=Node(val)
        print(f"Enter left child of {val}:")
        root.left=self.create()
        print(f"Enter right child of {val}:")
        root.right=self.create()
        return root
    def preorder(self,root):
        if root is not None:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")