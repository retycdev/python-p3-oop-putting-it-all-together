#!/usr/bin/env python3

# class Shoe:
#     pass

# lib/shoe.py
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Use a private variable for validation
        self.size = size   # Use the property setter for validation
        self.condition = None  # Initialize `condition` to `None`

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        """Repair the shoe and set its condition to 'New'."""
        self.condition = "New"
        print("Your shoe is as good as new!")
