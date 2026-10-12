class Book:
    def __init__(self, book):
        self.book = book
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def returnbook(self, x):                    # insert at beginning
        self.length += 1

        if self.top is None:              # if stack is empty
            self.top = Book(x)
            print("Returned : ",x)
            return

        else:
            newbook = Book(x)             # create new book
            newbook.next = self.top       # point to current top
            self.top = newbook            # make new book the top
            print("Returned : ",x)
            return

    def borrowbook(self):                        # delete at beginning
        if self.top == None:
            print("Stack is Empty")
            return

        self.length -= 1
        popped = self.top.book             # store top book
        self.top = self.top.next            # next book becomes top

        print("Borrowed : " + str(popped))
        return

    def peek(self):
        if self.top == None:
            print("Stack is Empty")
            return

        print("Top : " + str(self.top.book))

    def display(self):
        curr = self.top                   # start at top

        if self.top is None:
            print("Stack is empty")
            return

        result = "Stack: "

        while curr != None:                 #while curr is none
            result += str(curr.book)        #store current book in result

            if curr.next != None:           #if there is another book present after curr
                result += " "               #separate with space

            curr = curr.next                #traverse

        print(result)
        


# Create stack
stack1 = Stack()

# Number of operations
n = int(input())

# Store outputs
output = []

for i in range(n):
    operation = input().split()

    if operation[0] == "RETURN":
        book = " ".join(operation[1:])          #from first index onwards and join everything from there with spaces
        stack1.returnbook(book)
        output.append("Returned :" + book)

    elif operation[0] == "DISPLAY":
        output.append(stack1.display())

    elif operation[0] == "BORROW":
        output.append(stack1.borrowbook())

    elif operation[0] == "PEEK":
        output.append(stack1.peek())