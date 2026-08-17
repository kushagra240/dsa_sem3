"""Railway ticket counter queue implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Passenger:
    ticket_id: str
    status: str  # confirmed only


class RailwayTicketQueue:
    MAX_CAPACITY = 50

    def __init__(self) -> None:
        self._queue: List[Passenger] = []
        self._ticket_ids: set[str] = set()

    def enqueue(self, ticket_id: str, status: str) -> bool:
        if len(self._queue) >= self.MAX_CAPACITY:
            return False
        if status != "confirmed":
            return False
        if ticket_id in self._ticket_ids:
            return False

        passenger = Passenger(ticket_id=ticket_id, status=status)
        self._queue.append(passenger)
        self._ticket_ids.add(ticket_id)
        return True

    def dequeue(self) -> Optional[Passenger]:
        if not self._queue:
            return None
        passenger = self._queue.pop(0)
        self._ticket_ids.remove(passenger.ticket_id)
        return passenger

    def front(self) -> Optional[Passenger]:
        return self._queue[0] if self._queue else None

    def display(self) -> List[Passenger]:
        return list(self._queue)


if __name__ == "__main__":
    queue = RailwayTicketQueue()
    queue.enqueue("T001", "confirmed")
    queue.enqueue("T002", "confirmed")
    print("Front:", queue.front())
    print("Queue:", queue.display())
