stack=[]
def push():
    data=input("Enter Data of Libary:")
    stack.append(data)

def pop():
    print(f"poped item is{stack.pop()}")

def peek():
    print(f"All element are a s follow\n {stack[-1]}")

def display():
    print(f"All the element are follows\n{stack}")

while True:
    ch=int(input("1 for push\n2 for pop\n3 for peek\n4 for print\n"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        peek()
    else:
        display()
