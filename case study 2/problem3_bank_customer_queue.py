"""Bank customer queue implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Customer:
    token_number: str
    valid_token_holder: bool


class BankCustomerQueue:
    MAX_CAPACITY = 60

    def __init__(self) -> None:
        self._queue: List[Customer] = []
        self._token_numbers: set[str] = set()

    def enqueue(self, token_number: str, valid_token_holder: bool) -> bool:
        if len(self._queue) >= self.MAX_CAPACITY:
            return False
        if not valid_token_holder:
            return False
        if token_number in self._token_numbers:
            return False

        customer = Customer(
            token_number=token_number,
            valid_token_holder=valid_token_holder,
        )
        self._queue.append(customer)
        self._token_numbers.add(token_number)
        return True

    def dequeue(self) -> Optional[Customer]:
        if not self._queue:
            return None
        customer = self._queue.pop(0)
        self._token_numbers.remove(customer.token_number)
        return customer

    def front(self) -> Optional[Customer]:
        return self._queue[0] if self._queue else None

    def display(self) -> List[Customer]:
        return list(self._queue)


if __name__ == "__main__":
    queue = BankCustomerQueue()
    queue.enqueue("TK001", True)
    queue.enqueue("TK002", True)
    print("Next customer:", queue.front())
    print("Queue:", queue.display())
