"""Cafeteria plate stack implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Plate:
    plate_id: str
    material: str  # Steel or Ceramic


class PlateStack:
    MAX_CAPACITY = 20
    ALLOWED_MATERIALS = {"Steel", "Ceramic"}

    def __init__(self) -> None:
        self._stack: List[Plate] = []
        self._ids: set[str] = set()

    def push(self, plate_id: str, material: str) -> bool:
        if len(self._stack) >= self.MAX_CAPACITY:
            return False
        if material not in self.ALLOWED_MATERIALS:
            return False
        if plate_id in self._ids:
            return False

        plate = Plate(plate_id=plate_id, material=material)
        self._stack.append(plate)
        self._ids.add(plate_id)
        return True

    def pop(self) -> Optional[Plate]:
        if not self._stack:
            return None
        plate = self._stack.pop()
        self._ids.remove(plate.plate_id)
        return plate

    def peek(self) -> Optional[Plate]:
        return self._stack[-1] if self._stack else None

    def display(self) -> List[Plate]:
        return list(reversed(self._stack))


if __name__ == "__main__":
    stack = PlateStack()
    stack.push("P101", "Steel")
    stack.push("P102", "Ceramic")
    print("Top:", stack.peek())
    print("Stack:", stack.display())
