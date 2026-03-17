"""
Bubble Sort implementation module.

This module provides a basic implementation of the bubble sort algorithm,
which repeatedly steps through the list, compares adjacent elements, and
swaps them if they are in the wrong order.

Functions:
    bubbleSort(customList): Sorts a list in ascending order using bubble sort.

Time Complexity: O(N^2)
Space Complexity: O(1)
"""

import numpy as np

def bubbleSort(customList):
    """
    Sort a list using bubble sort algorithm.
    
    Implements bubble sort which compares adjacent elements and swaps them
    if they are in the wrong order. This process is repeated until the
    list is sorted.
    
    Args:
        customList (list): The list to be sorted (modified in-place).
    
    Returns:
        None (modifies the list in-place).
    
    Time Complexity: O(N^2) - quadratic time complexity
    Space Complexity: O(1) - constant space, sorts in-place
    """
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j+1] < customList[j]:
                customList[j+1], customList[j] = customList[j], customList[j+1]

cList = [2, 1, 7, 3, 45, 56, 23, 5, 9, 3]
cList = np.random.random_integers(0, 1000, 100)
print(cList)
bubbleSort(cList)
print(cList)

