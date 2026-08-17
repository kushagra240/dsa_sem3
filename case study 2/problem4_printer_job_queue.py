"""Printer job queue implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class PrintJob:
    job_id: str
    file_type: str


class PrinterJobQueue:
    MAX_CAPACITY = 30
    ALLOWED_TYPES = {"PDF", "DOCX"}

    def __init__(self) -> None:
        self._queue: List[PrintJob] = []
        self._job_ids: set[str] = set()

    def enqueue(self, job_id: str, file_type: str) -> bool:
        if len(self._queue) >= self.MAX_CAPACITY:
            return False
        if file_type not in self.ALLOWED_TYPES:
            return False
        if job_id in self._job_ids:
            return False

        job = PrintJob(job_id=job_id, file_type=file_type)
        self._queue.append(job)
        self._job_ids.add(job_id)
        return True

    def dequeue(self) -> Optional[PrintJob]:
        if not self._queue:
            return None
        job = self._queue.pop(0)
        self._job_ids.remove(job.job_id)
        return job

    def front(self) -> Optional[PrintJob]:
        return self._queue[0] if self._queue else None

    def display(self) -> List[PrintJob]:
        return list(self._queue)


if __name__ == "__main__":
    queue = PrinterJobQueue()
    queue.enqueue("J001", "PDF")
    queue.enqueue("J002", "DOCX")
    print("Next job:", queue.front())
    print("Queue:", queue.display())
