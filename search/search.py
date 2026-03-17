"""
Search algorithms module.

This module provides implementations of various search algorithms including
linear search, binary search, and several sorting algorithms used with search.

Functions:
    linearSearch(arr, val): Performs linear/sequential search.
    binarySearch(arr, val): Performs binary search on a sorted array.
    mergeSort(arr): Sorts array using merge sort.
    merge(left, right): Merges two sorted arrays.
    quickSort(arr, low, high): Sorts array using quick sort.
    partition(arr, low, high): Partitions array for quick sort.

Time Complexity: Linear search O(N), Binary search O(log N)
"""

def linearSearch(arr, val):
    """
    Perform a linear search to find a value in an array.
    
    Iterates through each element of the array to find the target value.
    Suitable for unsorted arrays.
    
    Args:
        arr (list): The array to search.
        val: The value to find.
    
    Returns:
        int: The index of the value if found, False otherwise.
    
    Time Complexity: O(N) - linear time
    Space Complexity: O(1) - constant space
    """
    for i,elm in enumerate(arr):
        if val == elm:
            return i
    return False

def binarySearch(arr, val):
    """
    Perform a binary search to find a value in a sorted array.
    
    Uses divide-and-conquer to efficiently search for a value in a sorted array
    by eliminating half of the remaining elements in each iteration.
    
    Args:
        arr (list): A sorted array to search.
        val: The value to find.
    
    Returns:
        int: The index of the value if found, -1 otherwise.
    
    Time Complexity: O(log N) - logarithmic time
    Space Complexity: O(1) - constant space
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def mergeSort(arr):
    """
    Sort an array using merge sort algorithm.
    
    Divides the array into halves recursively and merges them back together
    in sorted order. Efficient divide-and-conquer algorithm.
    
    Args:
        arr (list): The array to be sorted.
    
    Returns:
        list: The sorted array.
    
    Time Complexity: O(N log N) - divide and conquer
    Space Complexity: O(N) - creates new arrays
    """
    if len(arr) == 1:
        return arr
    
    start = 0
    end = len(arr)
    mid = (end + start)//2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted arrays into a single sorted array.
    
    Combines two sorted arrays by comparing elements and placing them
    in sorted order into a new array.
    
    Args:
        left (list): First sorted array.
        right (list): Second sorted array.
    
    Returns:
        list: A single sorted array containing all elements.
    
    Time Complexity: O(N) - single pass through both arrays
    Space Complexity: O(N) - creates new array
    """
    sortedList = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1
    sortedList.extend(left[i:])
    sortedList.extend(right[j:])
    return sortedList

def quickSort(arr, low=0, high=None):
    """
    Sort an array using quick sort algorithm.
    
    Uses a pivot-based partitioning approach to recursively sort subarrays
    divided by the pivot element. Efficient divide-and-conquer algorithm.
    
    Args:
        arr (list): The array to be sorted (modified in-place).
        low (int): Starting index for the sort (default: 0).
        high (int): Ending index for the sort (default: len(arr) - 1).
    
    Returns:
        None (modifies array in-place).
    
    Time Complexity: O(N log N) average, O(N^2) worst case
    Space Complexity: O(log N) - recursion stack space
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p)
        quickSort(arr, p + 1, high)

def partition(arr, low, high):
    """
    Partition an array for quick sort around a pivot element.
    
    Selects a pivot element and rearranges the subarray so elements smaller
    than the pivot are on the left and larger elements are on the right.
    
    Args:
        arr (list): The array being partitioned.
        low (int): Starting index of the partition.
        high (int): Ending index of the partition.
    
    Returns:
        int: The final position of the pivot.
    
    Time Complexity: O(N) - linear scan through partition
    Space Complexity: O(1) - constant space, in-place
    """
    pivot = arr[(low + high)//2]
    i = low
    j = high
    while True: 
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

import numpy as np
k = np.random.randint(0, 100, 100)
k = np.sort(k)
#print(k)
#print(binarySearch(k, -1000))    

l = np.random.randint(0, 100, 100)
sorted_l = mergeSort(l)
#print(l)
#print(np.array(sorted_l).astype(int))


m = np.random.randint(0, 100, 100)
print(m)
quickSort(m)
print(m)
#print(m)
#quickSort(m)
#print(m)


