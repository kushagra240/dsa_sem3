"""Library book return queue implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class ReturnedBook:
    book_id: str
    borrowed: bool


class LibraryBookReturnQueue:
    MAX_CAPACITY = 75

    def __init__(self) -> None:
        self._queue: List[ReturnedBook] = []
        self._book_ids: set[str] = set()

    def enqueue(self, book_id: str, borrowed: bool) -> bool:
        if len(self._queue) >= self.MAX_CAPACITY:
            return False
        if not borrowed:
            return False
        if book_id in self._book_ids:
            return False

        book = ReturnedBook(book_id=book_id, borrowed=borrowed)
        self._queue.append(book)
        self._book_ids.add(book_id)
        return True

    def dequeue(self) -> Optional[ReturnedBook]:
        if not self._queue:
            return None
        book = self._queue.pop(0)
        self._book_ids.remove(book.book_id)
        return book

    def front(self) -> Optional[ReturnedBook]:
        return self._queue[0] if self._queue else None

    def display(self) -> List[ReturnedBook]:
        return list(self._queue)


if __name__ == "__main__":
    queue = LibraryBookReturnQueue()
    queue.enqueue("B001", True)
    queue.enqueue("B002", True)
    print("Next book:", queue.front())
    print("Queue:", queue.display())
