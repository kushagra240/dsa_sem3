"""Single-lane parking garage stack implementation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Vehicle:
    registration_number: str
    vehicle_type: str  # Car or Bike


class ParkingGarage:
    MAX_CAPACITY = 10
    ALLOWED_TYPES = {"Car", "Bike"}

    def __init__(self) -> None:
        self._stack: List[Vehicle] = []
        self._registrations: set[str] = set()

    def push(self, registration_number: str, vehicle_type: str) -> bool:
        if len(self._stack) >= self.MAX_CAPACITY:
            return False
        if vehicle_type not in self.ALLOWED_TYPES:
            return False
        if registration_number in self._registrations:
            return False

        vehicle = Vehicle(
            registration_number=registration_number,
            vehicle_type=vehicle_type,
        )
        self._stack.append(vehicle)
        self._registrations.add(registration_number)
        return True

    def pop(self) -> Optional[Vehicle]:
        if not self._stack:
            return None
        vehicle = self._stack.pop()
        self._registrations.remove(vehicle.registration_number)
        return vehicle

    def peek(self) -> Optional[Vehicle]:
        return self._stack[-1] if self._stack else None

    def display(self) -> List[Vehicle]:
        return list(reversed(self._stack))


if __name__ == "__main__":
    garage = ParkingGarage()
    garage.push("KA01AB1234", "Car")
    garage.push("KA02CD5678", "Bike")
    print("Top vehicle:", garage.peek())
    print("Vehicles:", garage.display())
