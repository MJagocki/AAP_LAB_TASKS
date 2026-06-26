# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        # Ta metoda uruchamia się automatycznie przed KAŻDYM testem
        self.product = Product("Laptop", 2999.99, 10)

    def test_add_stock_positive(self):
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.product.add_stock(-2)

    def test_remove_stock_positive(self):
        self.product.remove_stock(3)
        self.assertEqual(self.product.quantity, 7)

    def test_remove_stock_too_much_raises(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(15)

    def test_remove_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(-5)

    def test_is_available_when_in_stock(self):
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        empty_product = Product("Klawiatura", 150.0, 0)
        self.assertFalse(empty_product.is_available())

    def test_total_value(self):
        # 2999.99 * 10 = 29999.9
        self.assertAlmostEqual(self.product.total_value(), 29999.9, places=1)

    def test_init_invalid_values(self):
        # Testy dodatkowe dla samego konstruktora
        with self.assertRaises(ValueError):
            Product("Błędny", -10.0, 5)
        with self.assertRaises(ValueError):
            Product("Błędny 2", 10.0, -5)


if __name__ == "__main__":
    unittest.main()
