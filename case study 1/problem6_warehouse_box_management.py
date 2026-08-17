"""Warehouse box stack implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Box:
    box_id: str
    weight_kg: float
    fragile: bool = False


class BoxStack:
    MAX_CAPACITY = 40

    def __init__(self) -> None:
        self._stack: List[Box] = []
        self._box_ids: set[str] = set()

    def push(self, box_id: str, weight_kg: float, fragile: bool = False) -> bool:
        if len(self._stack) >= self.MAX_CAPACITY:
            return False
        if box_id in self._box_ids:
            return False
        if weight_kg < 1 or weight_kg > 50:
            return False
        if fragile and weight_kg > 20:
            return False

        box = Box(box_id=box_id, weight_kg=weight_kg, fragile=fragile)
        self._stack.append(box)
        self._box_ids.add(box_id)
        return True

    def pop(self) -> Optional[Box]:
        if not self._stack:
            return None
        box = self._stack.pop()
        self._box_ids.remove(box.box_id)
        return box

    def peek(self) -> Optional[Box]:
        return self._stack[-1] if self._stack else None

    def display(self) -> List[Box]:
        return list(reversed(self._stack))


if __name__ == "__main__":
    stack = BoxStack()
    stack.push("B1", 12)
    stack.push("B2", 18, fragile=True)
    print("Top box:", stack.peek())
    print("Boxes:", stack.display())
