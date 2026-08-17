"""Case Study 20: Computer Lab Systems."""

from dataclasses import dataclass
from typing import Any, Iterable, Optional


@dataclass
class Node:
    data: Any
    next: Optional["Node"] = None


class SinglyLinkedList:
    def __init__(self, values: Iterable[Any] = ()) -> None:
        self.head: Optional[Node] = None
        for value in values:
            self.insert_at_end(value)

    def insert_at_end(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, data: Any) -> bool:
        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self) -> list[Any]:
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values


if __name__ == "__main__":
    ll = SinglyLinkedList(["PC1", "PC2", "PC3", "PC4", "PC5"])
    print("Systems:", ll.display())
    ll.delete("PC3")
    ll.insert_at_end("PC6")
    print("Updated systems:", ll.display())
    print("If PC10 is deleted: Data not found")
