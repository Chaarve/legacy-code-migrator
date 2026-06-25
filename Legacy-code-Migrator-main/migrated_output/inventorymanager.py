# Migrated from InventoryManager.java using AI Migration Agent
"""Inventory management module migrated to Python.
Preserves the original business logic of adding products, searching, and calculating total inventory value.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Product:
    """Represents a product with name, price, and quantity."""
    name: str
    price: float
    quantity: int

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def get_quantity(self) -> int:
        return self.quantity


class InventoryManager:
    """Manages a collection of Product instances."""

    def __init__(self) -> None:
        self.products: List[Product] = []

    def add_product(self, name: str, price: float, quantity: int) -> None:
        """Add a new product to the inventory.

        Args:
            name: Product name.
            price: Unit price.
            quantity: Number of units.
        """
        p = Product(name, price, quantity)
        self.products.append(p)
        print(f"Added: {name}")

    def find_product(self, name: str) -> Optional[Product]:
        """Find a product by name (case‑insensitive)."""
        for p in self.products:
            if p.get_name().lower() == name.lower():
                return p
        return None

    def calculate_total_value(self) -> float:
        """Calculate the total monetary value of all inventory items."""
        total = 0.0
        for p in self.products:
            total += p.get_price() * p.get_quantity()
        return total


def main() -> None:
    mgr = InventoryManager()
    mgr.add_product("Laptop", 999.99, 10)
    mgr.add_product("Mouse", 29.99, 50)
    print(f"Total value: ${mgr.calculate_total_value():.2f}")


if __name__ == "__main__":
    main()
