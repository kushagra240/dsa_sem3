class Book:
    def __init__(self, book):
        self.book = book
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, x):       #(at end)
        newbook = Book(x)

        if self.head is None:       #if head is not pointing to anything i.e. LL has no nodes right now
            self.head=newbook       #make newnode as the head
            print("Inserted : ",x)
            return
                                    
        curr=self.head              #else make head node the curr node
        while curr.next!=None:      #until curr reaches None
            curr=curr.next          #keep going to the next node
        curr.next=newbook
        print("Inserted : ",x)          #at the next pointer of current node (i.e the last node), join newnode

    def delete(self):                   #(at end)
        if self.head is None:           #if there are currently no nodes
            print("List is Empty")
            return      
            
        if self.head.next is None:                  #special case where LL has only one node
            removed = self.head.book                #store value to be deleted so we can print it
            self.head=None                          #set head to none, hence the LL is empty now
            print("Removed : " + removed)
            return
            
        curr=self.head                              #else make head node the curr node

        while curr.next.next!=None:                 #since last node is curr.next, penultimate node will be curr.next.next
            curr=curr.next                          #keep traversing while true

        removed = curr.next.book                    #store value to be deleted so we can print it
        curr.next=None                              #point next of penultimate node to None so that the last node will exit
        print("Removed : " + removed)        
       
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        curr = self.head
        result = "List: "
        while curr != None:
            result += curr.book

            if curr.next != None:
                result += " "
            curr = curr.next
        print(result)



# Create linked list
library = LinkedList()

# Number of operations
n = int(input())

# Store outputs
output = []

for i in range(n):
    operation = input().split()

    if operation[0] == "INSERT":
        book = " ".join(operation[1:])
        library.insert(book)
        output.append("Inserted: " + book)


    elif operation[0] == "DISPLAY":
        output.append(library.display())

    elif operation[0] == "REMOVE":
        output.append(library.delete())