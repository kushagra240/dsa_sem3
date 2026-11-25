class HashTable:
    def __init__(self):
        self.size = 10
        self.hash = [-1] * self.size

    def insert(self, key):
        if -1 not in self.hash:
            print("Hash Table is Full!")
            return

        index = key % self.size
        while self.hash[index] != -1:
            index = (index + 1) % self.size

        self.hash[index] = key
        print(key, "inserted at index", index)

    def display(self):
        print("\nIndex\tValue")
        for i in range(self.size):
            if self.hash[i] == -1:
                print(i, "\tEmpty")
            else:
                print(i, "\t", self.hash[i])


h = HashTable()
n = int(input("Enter number of keys: "))
print("Enter keys:")
for _ in range(n):
    h.insert(int(input()))

h.display()


class HashTable:
    def __init__(self):
        self.size = 10
        self.hash = [-1] * self.size

    def insert(self, key):
        if -1 not in self.hash:
            print("Hash Table is Full!")
            return

        index = key % self.size

        if self.hash[index] != -1 and self.hash[index] % self.size != index:
            print(self.hash[index], "is displaced from index", index)
            self.hash[index], key = key, self.hash[index]

        while self.hash[index] != -1:
            index = (index + 1) % self.size

        self.hash[index] = key

    def display(self):
        print("\nIndex\tValue")
        for i in range(self.size):
            if self.hash[i] == -1:
                print(i, "\tEmpty")
            else:
                print(i, "\t", self.hash[i])


h = HashTable()
n = int(input("Enter number of keys: "))
print("Enter keys:")
for _ in range(n):
    h.insert(int(input()))

h.display()