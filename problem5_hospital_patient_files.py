"""Hospital patient file stack implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class PatientFile:
    patient_id: str
    file_type: str  # Emergency or Priority


class PatientFileStack:
    MAX_CAPACITY = 50
    ALLOWED_TYPES = {"Emergency", "Priority"}

    def __init__(self) -> None:
        self._stack: List[PatientFile] = []
        self._patient_ids: set[str] = set()

    def push(self, patient_id: str, file_type: str) -> bool:
        if not patient_id:
            return False
        if file_type not in self.ALLOWED_TYPES:
            return False
        if len(self._stack) >= self.MAX_CAPACITY:
            return False
        if patient_id in self._patient_ids:
            return False

        patient_file = PatientFile(patient_id=patient_id, file_type=file_type)
        self._stack.append(patient_file)
        self._patient_ids.add(patient_id)
        return True

    def pop(self) -> Optional[PatientFile]:
        if not self._stack:
            return None
        patient_file = self._stack.pop()
        self._patient_ids.remove(patient_file.patient_id)
        return patient_file

    def peek(self) -> Optional[PatientFile]:
        return self._stack[-1] if self._stack else None

    def display(self) -> List[PatientFile]:
        return list(reversed(self._stack))


if __name__ == "__main__":
    stack = PatientFileStack()
    stack.push("PT1001", "Emergency")
    stack.push("PT1002", "Priority")
    print("Top file:", stack.peek())
    print("Files:", stack.display())
