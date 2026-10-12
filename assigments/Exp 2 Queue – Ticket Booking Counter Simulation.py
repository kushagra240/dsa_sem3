class Customer:
    def __init__(self, name):
        self.name = name
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, x):
        newcustomer = Customer(x)
        self.length += 1

        if self.front is None:
            self.front = newcustomer
            self.rear = newcustomer
            print("Waiting : ",x)
            return
        else:
            self.rear.next = newcustomer
            self.rear = newcustomer
            print("Waiting : ",x)
            return

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty.")
            return

        self.length -= 1
        customer = self.front.name
        self.front = self.front.next

        if self.front is None:         #in case there was only one node which is now dequeued
            self.rear = None

        print("Served : " + customer)

    def display(self):
        curr = self.front
        if self.front is None:
            print("Queue is Empty")
            return

        result = "Queue: "

        while curr != None:
            result += curr.name
            if curr.next != None:
                result += " "
            curr = curr.next
        print(result)

    def peek(self):
        if self.front == None:
            print("Queue is Empty")
            return
        print("Next : " + self.front.name)


# Create queue
queue1 = Queue()

# Number of operations
n = int(input())

# Store outputs
output = []

for i in range(n):
    operation = input().split()

    if operation[0] == "ENQUEUE":
        name = " ".join(operation[1:])
        queue1.enqueue(name)
        output.append("Enqueued : " + name)

    elif operation[0] == "DISPLAY":
        output.append(queue1.display())

    elif operation[0] == "DEQUEUE":
        output.append(queue1.dequeue())

    elif operation[0] == "PEEK":
        output.append(queue1.peek())