"""Supermarket billing queue implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class BillingCustomer:
    customer_id: str
    has_shopping_cart: bool


class SupermarketBillingQueue:
    MAX_CAPACITY = 40

    def __init__(self) -> None:
        self._queue: List[BillingCustomer] = []
        self._customer_ids: set[str] = set()

    def enqueue(self, customer_id: str, has_shopping_cart: bool) -> bool:
        if len(self._queue) >= self.MAX_CAPACITY:
            return False
        if not has_shopping_cart:
            return False
        if customer_id in self._customer_ids:
            return False

        customer = BillingCustomer(
            customer_id=customer_id,
            has_shopping_cart=has_shopping_cart,
        )
        self._queue.append(customer)
        self._customer_ids.add(customer_id)
        return True

    def dequeue(self) -> Optional[BillingCustomer]:
        if not self._queue:
            return None
        customer = self._queue.pop(0)
        self._customer_ids.remove(customer.customer_id)
        return customer

    def front(self) -> Optional[BillingCustomer]:
        return self._queue[0] if self._queue else None

    def display(self) -> List[BillingCustomer]:
        return list(self._queue)


if __name__ == "__main__":
    queue = SupermarketBillingQueue()
    queue.enqueue("C001", True)
    queue.enqueue("C002", True)
    print("Next customer:", queue.front())
    print("Queue:", queue.display())
