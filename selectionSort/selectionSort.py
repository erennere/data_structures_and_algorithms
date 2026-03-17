"""
Selection Sort implementation module.

This module provides a basic implementation of the selection sort algorithm,
which divides the list into a sorted and unsorted portion, repeatedly finding
the minimum element from the unsorted portion and moving it to the sorted portion.

Functions:
    selectionSort(customList): Sorts a list in ascending order using selection sort.

Time Complexity: O(N^2)
Space Complexity: O(1)
"""

import numpy as np

#Time complexity O(N^2)
#Space complexity O(1)
def selectionSort(customList):
    """
    Sort a list using selection sort algorithm.
    
    Implements selection sort which repeatedly finds the minimum element from
    the unsorted portion of the list and places it in the sorted portion.
    
    Args:
        customList (list): The list to be sorted (modified in-place).
    
    Returns:
        None (modifies the list in-place).
    
    Time Complexity: O(N^2) - quadratic time complexity
    Space Complexity: O(1) - constant space, sorts in-place
    """
    for i in range(len(customList)):
        minimum = customList[i]
        index = i
        for j in range(i+1, len(customList)):
            if customList[j] < minimum:
                minimum = customList[j]
                index = j
        customList[i], customList[index] = customList[index], customList[i]

cList = np.random.random_integers(0, 100, 250)
print(cList)
selectionSort(cList)
print(cList)

