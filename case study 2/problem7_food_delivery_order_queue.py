"""Food delivery order queue implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class FoodOrder:
    order_id: str
    confirmed: bool


class FoodDeliveryOrderQueue:
    MAX_CAPACITY = 100

    def __init__(self) -> None:
        self._queue: List[FoodOrder] = []
        self._order_ids: set[str] = set()

    def enqueue(self, order_id: str, confirmed: bool) -> bool:
        if len(self._queue) >= self.MAX_CAPACITY:
            return False
        if not confirmed:
            return False
        if order_id in self._order_ids:
            return False

        order = FoodOrder(order_id=order_id, confirmed=confirmed)
        self._queue.append(order)
        self._order_ids.add(order_id)
        return True

    def dequeue(self) -> Optional[FoodOrder]:
        if not self._queue:
            return None
        order = self._queue.pop(0)
        self._order_ids.remove(order.order_id)
        return order

    def front(self) -> Optional[FoodOrder]:
        return self._queue[0] if self._queue else None

    def display(self) -> List[FoodOrder]:
        return list(self._queue)


if __name__ == "__main__":
    queue = FoodDeliveryOrderQueue()
    queue.enqueue("O001", True)
    queue.enqueue("O002", True)
    print("Next order:", queue.front())
    print("Queue:", queue.display())
