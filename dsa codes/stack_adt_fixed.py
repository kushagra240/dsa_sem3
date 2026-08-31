"""Stack ADT implementation using a fixed-size array.

This program implements a stack using an array with a TOP pointer.
It supports push, pop, peek, display, and checks for stack overflow
and underflow conditions.
"""


class Stack:
    def __init__(self, size=100):
        self.MAX_SIZE = size
        self.TOP = -1
        self.st = [0] * self.MAX_SIZE

    def is_empty(self):
        return self.TOP == -1

    def is_full(self):
        return self.TOP == self.MAX_SIZE - 1

    def push(self, x):
        if self.is_full():
            print("Stack Overflow")
            return False

        self.TOP += 1
        self.st[self.TOP] = x
        return True

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None

        x = self.st[self.TOP]
        self.TOP -= 1
        return x

    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        return self.st[self.TOP]

    def display(self):
        if self.is_empty():
            print("Stack is Empty")
            return

        print("Stack elements are:")
        for i in range(self.TOP, -1, -1):
            print(self.st[i])


def main():
    s = Stack(5)

    print("Stack ADT Demo")
    print("=" * 20)

    s.push(10)
    s.push(20)
    s.push(30)
    s.display()

    print("Top element:", s.peek())
    print("Popped element:", s.pop())
    print("Top element after pop:", s.peek())

    s.push(40)
    s.push(50)
    s.push(60)  # This will cause Stack Overflow

    print("Final stack:")
    s.display()


if __name__ == "__main__":
    main()
