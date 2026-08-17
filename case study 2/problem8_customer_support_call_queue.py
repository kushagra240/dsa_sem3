"""Customer support call queue implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class SupportCall:
    call_id: str
    active: bool


class CustomerSupportCallQueue:
    MAX_CAPACITY = 80

    def __init__(self) -> None:
        self._queue: List[SupportCall] = []
        self._call_ids: set[str] = set()

    def enqueue(self, call_id: str, active: bool) -> bool:
        if len(self._queue) >= self.MAX_CAPACITY:
            return False
        if not active:
            return False
        if call_id in self._call_ids:
            return False

        call = SupportCall(call_id=call_id, active=active)
        self._queue.append(call)
        self._call_ids.add(call_id)
        return True

    def dequeue(self) -> Optional[SupportCall]:
        if not self._queue:
            return None
        call = self._queue.pop(0)
        self._call_ids.remove(call.call_id)
        return call

    def front(self) -> Optional[SupportCall]:
        return self._queue[0] if self._queue else None

    def display(self) -> List[SupportCall]:
        return list(self._queue)


if __name__ == "__main__":
    queue = CustomerSupportCallQueue()
    queue.enqueue("CL001", True)
    queue.enqueue("CL002", True)
    print("Next call:", queue.front())
    print("Queue:", queue.display())
