"""Browser history stack implementation."""

from typing import List, Optional


class BrowserHistory:
    MAX_CAPACITY = 15

    def __init__(self) -> None:
        self._history: List[str] = []

    def push(self, url: str) -> bool:
        if len(self._history) >= self.MAX_CAPACITY:
            return False
        if not url.startswith("https://"):
            return False
        if self._history and self._history[-1] == url:
            return False

        self._history.append(url)
        return True

    def pop(self) -> Optional[str]:
        if not self._history:
            return None
        return self._history.pop()

    def peek(self) -> Optional[str]:
        return self._history[-1] if self._history else None

    def display(self) -> List[str]:
        return list(reversed(self._history))


if __name__ == "__main__":
    history = BrowserHistory()
    history.push("https://example.com")
    history.push("https://openai.com")
    print("Current:", history.peek())
    print("History:", history.display())
