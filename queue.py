class queue:
    def __init__(self):
        self.front=-1
        self.rear=-1
        self.qt=[0]*5
    
    def insert(self,x):
        if self.rear==4:
            print("Queue Overflow !!")
            return
        self.rear=self.rear+1
        self.qt[self.rear]=x

        if self.front==-1:
            self.front=0
    
    def delete(self):
        if self.front==-1:
            print("Nothing to print...empty queue")
            return None

        x=self.qt[self.front]

        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=self.front+1
        return x
    
    def peek(self):
        if self.front == -1:
            print("Queue is empty !!")
            return None
        return self.qt[self.front]
    
    def display(self):
        if self.front==-1:
            print("Queue underflow !!")

        for i in range(self.front,self.rear+1):
            print(self.qt[i]," ")

q=queue()

while True:
    ch = int(input("1 for insert\n2 for delete\n3 for display\n4 for peek\n5 for exit\n"))
    if ch == 1:
        data = int(input("Enter a number in queue: "))
        q.insert(data)
    elif ch == 2:
        q.delete()
    elif ch == 3:
        q.display()
    elif ch == 4:
        val=q.peek()
        print("Top value is ",val)
    else:
        break