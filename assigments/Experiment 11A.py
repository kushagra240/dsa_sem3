def heapify(arr, n, i, is_max):
    best = i
    left = 2 * i + 1
    right = 2 * i + 2

    if is_max:
        if left < n and arr[left] > arr[best]:
            best = left
        if right < n and arr[right] > arr[best]:
            best = right
    else:
        if left < n and arr[left] < arr[best]:
            best = left
        if right < n and arr[right] < arr[best]:
            best = right

    if best != i:
        arr[i], arr[best] = arr[best], arr[i]
        heapify(arr, n, best, is_max)


def heap_sort(nums, is_max):
    arr = nums.copy()
    n = len(arr)

    # 1. Build heap (from last non-leaf node up to root)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, is_max)

    # 2. Swap root with last element, shrink heap, and heapify root
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0, is_max)

    return arr


def main():
    n = int(input("Enter number of elements: "))
    if n < 0:
        print("Number of elements cannot be negative.")
        return
    numbers = []
    for _ in range(n):
        numbers.append(int(input("Enter element: ")))
    print("\n1. Min Heap - Descending Order")
    print("2. Max Heap - Ascending Order")
    choice = int(input("Enter your choice: "))
    print("\nOriginal list:", numbers)
    if choice == 1:
        result = heap_sort(numbers, is_max=False)
        print("Sorted list (Descending using Min Heap):", result)
    elif choice == 2:
        result = heap_sort(numbers, is_max=True)
        print("Sorted list (Ascending using Max Heap):", result)
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()