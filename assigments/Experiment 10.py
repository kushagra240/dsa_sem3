class HashTable:
    def __init__(self, size, replacement=False):
        self.size = size
        self.table = [None] * size
        self.replacement = replacement

    def insert(self, key):
        if key in self.table:
            print("Duplicate key:", key)
            return
        if None not in self.table:
            print("Hash table is full. Cannot insert", key)
            return
        home = key % self.size
        if not self.replacement:
            pos = home
            while self.table[pos] is not None:
                pos = (pos + 1) % self.size
            self.table[pos] = key
            return

        pos = home
        while self.table[pos] is not None:
            if self.table[pos] % self.size != pos:
                self.table[pos], key = key, self.table[pos]
            pos = (pos + 1) % self.size
        self.table[pos] = key

    def search(self, key):
        home = key % self.size
        for step in range(self.size):
            pos = (home + step) % self.size
            if self.table[pos] is None:
                return -1
            if self.table[pos] == key:
                return pos
        return -1

    def display(self):
        print("\nIndex\tKey")
        print("----------------")
        for i, val in enumerate(self.table):
            print(i, "\t", val if val is not None else "EMPTY")


def main():
    size = int(input("Enter hash table size: "))
    choice = int(input("Choose collision handling (1: Without replacement, 2: With replacement): "))
    if choice not in (1, 2):
        print("Invalid choice.")
        return
    if size <= 0:
        return
    ht = HashTable(size, replacement=(choice == 2))
    n = int(input("Enter number of keys to insert: "))
    for _ in range(n):
        ht.insert(int(input("Enter key: ")))
    ht.display()
    target = int(input("\nEnter key to search: "))
    position = ht.search(target)
    if position != -1:
        print("Key found at index", position)
    else:
        print("Key not found")


if __name__ == "__main__":
    main()