"""Restaurant tray stack implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Tray:
    tray_number: str
    status: str  # Clean only


class TrayStack:
    MAX_CAPACITY = 30

    def __init__(self) -> None:
        self._stack: List[Tray] = []
        self._tray_numbers: set[str] = set()

    def push(self, tray_number: str, status: str) -> bool:
        if len(self._stack) >= self.MAX_CAPACITY:
            return False
        if status != "Clean":
            return False
        if tray_number in self._tray_numbers:
            return False

        tray = Tray(tray_number=tray_number, status=status)
        self._stack.append(tray)
        self._tray_numbers.add(tray_number)
        return True

    def pop(self) -> Optional[Tray]:
        if not self._stack:
            return None
        tray = self._stack.pop()
        self._tray_numbers.remove(tray.tray_number)
        return tray

    def peek(self) -> Optional[Tray]:
        return self._stack[-1] if self._stack else None

    def display(self) -> List[Tray]:
        return list(reversed(self._stack))


if __name__ == "__main__":
    stack = TrayStack()
    stack.push("T1", "Clean")
    stack.push("T2", "Clean")
    print("Top tray:", stack.peek())
    print("Tray stack:", stack.display())
