"""
This module contains a simple class modeling an apple basket.
Apples may be added or removed from basket.
¡¡¡The basket has a maxium size!!
"""

class AppleBasket:
    def __init__(self, initial_count=0, max_count=15):
        if initial_count < 0:
            raise ValueError("Initial apple basket count must not be negative (-) ")
        if max_count < 0:
            raise ValueError("Max apple basket count must not be negative (-) ")
        
        self._count = initial_count
        self._max_count = max_count
    
    @property
    def count(self):
        return self._count
    
    @property
    def is_full(self):
        return self.count == self.max_count
    
    @property
    def is_empty(self):
        return self.count == 0
    
    @property
    def max_count(self):
        return self._max_count
    
    def add(self, count=1):
        new_count = self.count + count
        if new_count > self.max_count:
            raise ValueError("Attemped to add too many apples")
        self._count = new_count
    
    def remove(self, count=1):
        new_count = self.count - count
        if new_count < 0:
            raise ValueError("Attempted to remove too many apples")
        self._count = new_count
    