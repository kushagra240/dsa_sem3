"""Airport check-in queue implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class CheckInPassenger:
    boarding_pass_id: str
    valid_ticket: bool


class AirportCheckInQueue:
    MAX_CAPACITY = 150

    def __init__(self) -> None:
        self._queue: List[CheckInPassenger] = []
        self._boarding_pass_ids: set[str] = set()

    def enqueue(self, boarding_pass_id: str, valid_ticket: bool) -> bool:
        if len(self._queue) >= self.MAX_CAPACITY:
            return False
        if not valid_ticket:
            return False
        if boarding_pass_id in self._boarding_pass_ids:
            return False

        passenger = CheckInPassenger(
            boarding_pass_id=boarding_pass_id,
            valid_ticket=valid_ticket,
        )
        self._queue.append(passenger)
        self._boarding_pass_ids.add(boarding_pass_id)
        return True

    def dequeue(self) -> Optional[CheckInPassenger]:
        if not self._queue:
            return None
        passenger = self._queue.pop(0)
        self._boarding_pass_ids.remove(passenger.boarding_pass_id)
        return passenger

    def front(self) -> Optional[CheckInPassenger]:
        return self._queue[0] if self._queue else None

    def display(self) -> List[CheckInPassenger]:
        return list(self._queue)


if __name__ == "__main__":
    queue = AirportCheckInQueue()
    queue.enqueue("BP1001", True)
    queue.enqueue("BP1002", True)
    print("Next passenger:", queue.front())
    print("Queue:", queue.display())
