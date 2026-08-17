"""Hospital patient queue implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Patient:
    patient_id: str
    registered: bool


class HospitalPatientQueue:
    MAX_CAPACITY = 100

    def __init__(self) -> None:
        self._queue: List[Patient] = []
        self._patient_ids: set[str] = set()

    def enqueue(self, patient_id: str, registered: bool) -> bool:
        if len(self._queue) >= self.MAX_CAPACITY:
            return False
        if not registered:
            return False
        if patient_id in self._patient_ids:
            return False

        patient = Patient(patient_id=patient_id, registered=registered)
        self._queue.append(patient)
        self._patient_ids.add(patient_id)
        return True

    def dequeue(self) -> Optional[Patient]:
        if not self._queue:
            return None
        patient = self._queue.pop(0)
        self._patient_ids.remove(patient.patient_id)
        return patient

    def front(self) -> Optional[Patient]:
        return self._queue[0] if self._queue else None

    def display(self) -> List[Patient]:
        return list(self._queue)


if __name__ == "__main__":
    queue = HospitalPatientQueue()
    queue.enqueue("P100", True)
    queue.enqueue("P101", True)
    print("Next patient:", queue.front())
    print("Queue:", queue.display())
