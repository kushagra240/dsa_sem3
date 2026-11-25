class HeapSort:
    def read(self):
        self.n = int(input("Enter number of elements: "))
        print("Enter elements:")
        self.a = [int(input()) for _ in range(self.n)]

    def heapify(self, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.a[left] < self.a[smallest]:
            smallest = left
        if right < n and self.a[right] < self.a[smallest]:
            smallest = right

        if smallest != i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.heapify(n, smallest)

    def sort(self):
        for i in range(self.n // 2 - 1, -1, -1):
            self.heapify(self.n, i)
        for i in range(self.n - 1, 0, -1):
            self.a[0], self.a[i] = self.a[i], self.a[0]
            self.heapify(i, 0)

    def display(self):
        print("\nSorted elements in Descending Order:")
        for i in range(self.n):
            print(self.a[i], end=" ")
        print()


h = HeapSort()
h.read()
h.sort()
h.display()

class HeapSort:
    def read(self):
        self.n = int(input("Enter number of elements: "))
        print("Enter elements:")
        self.a = [int(input()) for _ in range(self.n)]

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.a[left] > self.a[largest]:
            largest = left
        if right < n and self.a[right] > self.a[largest]:
            largest = right

        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.heapify(n, largest)

    def sort(self):
        for i in range(self.n // 2 - 1, -1, -1):
            self.heapify(self.n, i)
        for i in range(self.n - 1, 0, -1):
            self.a[0], self.a[i] = self.a[i], self.a[0]
            self.heapify(i, 0)

    def display(self):
        print("\nSorted elements in Ascending Order:")
        for i in range(self.n):
            print(self.a[i], end=" ")
        print()


h = HeapSort()
h.read()
h.sort()
h.display()