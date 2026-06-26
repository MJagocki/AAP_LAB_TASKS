# -*- coding: utf-8 -*-
class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Cena (price) nie może być ujemna.")
        if quantity < 0:
            raise ValueError("Ilość (quantity) nie może być ujemna.")
            
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Nie można dodać ujemnej ilości do magazynu.")
        self.quantity += amount

    def remove_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Nie można usunąć ujemnej ilości z magazynu.")
        if amount > self.quantity:
            raise ValueError("Próba usunięcia większej ilości niż dostępna w magazynie.")
        self.quantity -= amount

    def is_available(self) -> bool:
        return self.quantity > 0

    def total_value(self) -> float:
        return self.price * self.quantity
