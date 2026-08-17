"""Online customer order queue implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class CustomerOrder:
    order_id: str
    paid: bool


class OnlineCustomerOrderQueue:
    MAX_CAPACITY = 200

    def __init__(self) -> None:
        self._queue: List[CustomerOrder] = []
        self._order_ids: set[str] = set()

    def enqueue(self, order_id: str, paid: bool) -> bool:
        if len(self._queue) >= self.MAX_CAPACITY:
            return False
        if not paid:
            return False
        if order_id in self._order_ids:
            return False

        order = CustomerOrder(order_id=order_id, paid=paid)
        self._queue.append(order)
        self._order_ids.add(order_id)
        return True

    def dequeue(self) -> Optional[CustomerOrder]:
        if not self._queue:
            return None
        order = self._queue.pop(0)
        self._order_ids.remove(order.order_id)
        return order

    def front(self) -> Optional[CustomerOrder]:
        return self._queue[0] if self._queue else None

    def display(self) -> List[CustomerOrder]:
        return list(self._queue)


if __name__ == "__main__":
    queue = OnlineCustomerOrderQueue()
    queue.enqueue("ORD001", True)
    queue.enqueue("ORD002", True)
    print("Next order:", queue.front())
    print("Queue:", queue.display())
