"""Binary Heap helper module for insertion sort.

This module provides a simple Heap class for use in insertion sort operations,
using a list-based binary heap implementation with efficient insertion.
"""

class Heap:
    def __init__(self, value):
        """Initialize a heap with an initial value.
        
        Args:
            value: The first value to insert into the heap.
        """
        self.list = [value]
        self.length = 1

    def push(self, value):
        """Push a value onto the heap while maintaining heap property.
        
        Inserts the value at the end and then shifts it up to the correct position
        using the bubble-up (percolate-up) algorithm.
        
        Args:
            value: The value to push onto the heap.
        """
        self.list.append(value)
        i = len(self.list) - 1
        
        while i > 0:
            parent = (i - 1) // 2
            if self.list[parent] > value:
                self.list[i] = self.list[parent]
                i = parent
            else:
                break
        self.list[i] = value
