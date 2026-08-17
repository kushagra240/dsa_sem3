"""Call stack implementation for programming functions."""

from typing import List, Optional


class CallStack:
    MAX_DEPTH = 15
    MAX_RECURSION_LEVEL = 3

    def __init__(self) -> None:
        self._stack: List[str] = []

    @staticmethod
    def _is_valid_function_name(name: str) -> bool:
        return bool(name) and name[0].isalpha() and all(
            ch.isalnum() or ch == "_" for ch in name[1:]
        )

    def push(self, function_name: str) -> bool:
        if not self._is_valid_function_name(function_name):
            return False
        if len(self._stack) >= self.MAX_DEPTH:
            return False

        recursion_depth = 1
        if self._stack and self._stack[-1] == function_name:
            recursion_depth = 1
            for existing in reversed(self._stack):
                if existing == function_name:
                    recursion_depth += 1
                else:
                    break
        if recursion_depth > self.MAX_RECURSION_LEVEL:
            return False

        self._stack.append(function_name)
        return True

    def pop(self) -> Optional[str]:
        if not self._stack:
            return None
        return self._stack.pop()

    def peek(self) -> Optional[str]:
        return self._stack[-1] if self._stack else None

    def display(self) -> List[str]:
        return list(reversed(self._stack))


if __name__ == "__main__":
    stack = CallStack()
    stack.push("main")
    stack.push("helper")
    print("Current function:", stack.peek())
    print("Call stack:", stack.display())
