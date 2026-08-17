"""Undo stack for text editor actions."""

from typing import List, Optional


class TextEditorUndoStack:
    MAX_CAPACITY = 25
    ALLOWED_ACTIONS = {"Insert", "Delete", "Replace"}

    def __init__(self) -> None:
        self._actions: List[str] = []

    def push(self, action: str) -> bool:
        if action not in self.ALLOWED_ACTIONS:
            return False
        if len(self._actions) >= self.MAX_CAPACITY:
            return False
        if self._actions and self._actions[-1] == action:
            return False

        self._actions.append(action)
        return True

    def pop(self) -> Optional[str]:
        if not self._actions:
            return None
        return self._actions.pop()

    def peek(self) -> Optional[str]:
        return self._actions[-1] if self._actions else None

    def display(self) -> List[str]:
        return list(reversed(self._actions))


if __name__ == "__main__":
    stack = TextEditorUndoStack()
    stack.push("Insert")
    stack.push("Delete")
    print("Last action:", stack.peek())
    print("Actions:", stack.display())
