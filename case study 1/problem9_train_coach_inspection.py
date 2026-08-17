"""Train coach inspection report stack implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Report:
    report_number: str
    status: str  # Pending only


class ReportStack:
    MAX_CAPACITY = 25

    def __init__(self) -> None:
        self._stack: List[Report] = []
        self._report_numbers: set[str] = set()

    def push(self, report_number: str, status: str) -> bool:
        if not report_number:
            return False
        if status != "Pending":
            return False
        if len(self._stack) >= self.MAX_CAPACITY:
            return False
        if report_number in self._report_numbers:
            return False

        report = Report(report_number=report_number, status=status)
        self._stack.append(report)
        self._report_numbers.add(report_number)
        return True

    def pop(self) -> Optional[Report]:
        if not self._stack:
            return None
        report = self._stack.pop()
        self._report_numbers.remove(report.report_number)
        return report

    def peek(self) -> Optional[Report]:
        return self._stack[-1] if self._stack else None

    def display(self) -> List[Report]:
        return list(reversed(self._stack))


if __name__ == "__main__":
    stack = ReportStack()
    stack.push("R001", "Pending")
    stack.push("R002", "Pending")
    print("Latest report:", stack.peek())
    print("Reports:", stack.display())
