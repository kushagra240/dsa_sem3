class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):
            self.head=None

    def create(self):
         n=int(input("Enter no. of nodes:"))

         if n<=0:
            print("Enter valid no. of nodes")
            return

         for i in range(1,n+1):    
            val= input(f"Enter the value for node {i}:")
            self.insert(val)

    def insert(self,val):
        new_node=Node(val)

        if self.head==None:
            self.head=new_node
            return

        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node

    def delete(self,val):
        if self.head is None:
            print("Nothing is there to delete....")
            return

        if self.head.data==val:
            self.head=self.head.next
            print(f"Node {val} is deleted.")
            return
        
        prev=self.head
        temp=self.head.next
        while temp is not None:
            if temp.data == val:
                prev.next=temp.next
                print(f"Node {val} is deleted.")
                return
            prev=temp
            temp=temp.next
        print(f"Node {val} not found.")


    def display(self):
        if self.head is None:
            print("Linked List is empty...")
            return
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    my_list = ll()
    my_list.create()
    print("\nYour created Linked List:")
    my_list.display()
    
    target = input("\nEnter value to delete: ")
    my_list.delete(target) 
    
    print("\nUpdated Linked List:")
    my_list.display()