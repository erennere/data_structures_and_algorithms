"""
Sorting algorithms module (Insertion, Bucket, Merge, and Quick Sort).

This module provides implementations of multiple sorting algorithms including
insertion sort, bucket sort, merge sort, and quick sort (both recursive and iterative).

Functions:
    insertSort(customList): Sorts a list using insertion sort.
    bucketSort(customList): Sorts a list using bucket sort.
    mergeSort(customList): Sorts a list using merge sort.
    quickSort(customList): Sorts a list using quick sort (recursive).
    quickSort_iterative(customList): Sorts a list using quick sort (iterative).
    iterative_step(customList, start, stop): Helper for iterative quick sort.

Each function sorts the list and returns the sorted result.
"""

import numpy as np
import math

# space complexity O(1)
# time complexity O(N^2)
def insertSort(customList):
    """
    Sort a list using insertion sort algorithm.
    
    Sorting is achieved by building the sorted array one element at a time.
    Each element is removed from the unsorted portion, compared with elements
    in the already-sorted portion, and inserted into its correct position.
    This grows the sorted portion from left to right until the entire array is sorted.
    
    Args:
        customList (list): The list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Time Complexity: O(N^2) - quadratic time complexity
    Space Complexity: O(1) - constant space, sorts in-place
    """
    for i in range(1, len(customList)):
        elm = customList[i]
        j = i - 1
        while j >= 0 and elm < customList[j]:
            customList[j+1] = customList[j]
            j-= 1
        customList[j + 1] = elm
    return customList
            
# space complexity O(N)
# time complexity O() will change depending on the sorting method used 
def bucketSort(customList):
    """
    Sort a list using bucket sort algorithm.
    
    Sorting is achieved by distributing elements into multiple buckets based on
    their value ranges, sorting each bucket individually (using insertion sort),
    and then concatenating all buckets in order. This distributes the sorting work
    across buckets, reducing comparisons compared to sorting the entire array at once.
    
    Args:
        customList (list): The list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Time Complexity: O(N log N) average case - depends on insertion sort
    Space Complexity: O(N) - creates a new list and buckets
    """
    n = round(math.sqrt(len(customList)))
    max_value = max(customList)
    temp = [[] for i in range(n)]
    
    for i in customList:
        j = math.ceil(i * n / max_value)
        temp[j-1].append(i)

    for i in range(len(temp)):
        temp[i] = insertSort(temp[i])

    return [float(i) for templist in temp for i in templist]

# space complexity O(N) -- a new list is created
# time complexity O(Nlog(N)) due to the recursive nature, divide and conquer
def mergeSort(customList):
    """
    Sort a list using merge sort algorithm.
    
    Sorting is achieved using divide-and-conquer: the array is recursively divided
    into single elements (divide phase), then pairs of elements are merged in sorted
    order (conquer phase), progressively combining larger sorted sublists until the
    entire array is sorted. The merge operation maintains sorted order by comparing
    elements from two sublists consecutively.
    
    Args:
        customList (list): The list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Time Complexity: O(N log N) - divide and conquer approach
    Space Complexity: O(N) - creates new lists for merging
    """
    if len(customList) <= 1:
        return customList
    
    def merge(someList, l, r):
        """
        Merge two sorted sublists into a single sorted list.
        
        Merging is achieved by comparing elements from the left and right sorted
        sublists consecutively, adding the smaller element to the result, and
        advancing in that sublist. This maintains sorted order while combining
        two sorted portions into one.
        
        Args:
            someList (list): The list containing the sublists to merge.
            l (int): Starting index of the left sublist.
            r (int): Ending index of the right sublist.
        
        Returns:
            list: A sorted list containing all elements from l to r.
        """
        if r == l:
            return [someList[l]]

        sorted_list = []
        m = (l + r) // 2
        left = merge(someList, l, m)
        right = merge(someList, m+1 , r)
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list
    
    return merge(customList, 0, len(customList)-1)

def quickSort(customList):
    """
    Sort a list using quick sort algorithm (recursive implementation).
    
    Sorting is achieved using divide-and-conquer: a pivot element is selected,
    the array is partitioned so elements smaller than the pivot move left and
    larger elements move right, then quicksort is recursively applied to both
    partitions. This divides the problem into smaller subproblems that are
    solved independently.
    
    Implements a divide-and-conquer approach that selects a pivot element
    and partitions the list into elements less than and greater than the pivot.
    
    Args:
        customList (list): The list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Time Complexity: O(N log N) average case, O(N^2) worst case
    Space Complexity: O(N) - creates new lists during recursion
    """
    if len(customList) <= 1:
        return customList
    
    pivot = customList[0]
    left = [i for i in customList[1:] if i < pivot]
    right = [i for i in customList[1:] if i >= pivot]

    left = quickSort(left)
    right = quickSort(right)
    
    left.append(pivot)
    left.extend(right)
    return left

def quickSort_iterative(customList):
    """Sort a list using quick sort algorithm (iterative implementation).
    
    Sorting is achieved using divide-and-conquer with an explicit stack instead of
    recursion: ranges to be sorted are pushed on the stack, the top range is popped
    and partitioned around a pivot, then the left and right partitions are pushed
    consecutively for processing. This achieves the same divide-and-conquer effect
    while avoiding recursive function call overhead.
    
    
    Args:
        customList (list): The list to be sorted (modified in-place).
    
    Returns:
        list: The sorted list.
    
    Time Complexity: O(N log N) average case, O(N^2) worst case
    Space Complexity: O(log N) - iterative stack space instead of recursion
    """
    stack = [(0, len(customList))]
    while stack:
        start, stop = stack.pop()
        if stop - start <= 1:
            continue

        swap = iterative_step(customList, start, stop)
        stack.append((start, swap))
        stack.append((swap+1, stop))
    return customList

def iterative_step(customList, start, stop):
    """
    Perform one partitioning step for iterative quick sort.
    
    Selects a pivot and partitions the subarray, moving the pivot to its
    correct position and returning that position.
    
    Args:
        customList (list): The list being sorted.
        start (int): Starting index of the partition.
        stop (int): Ending index of the partition.
    
    Returns:
        int: The final position of the pivot in the sorted partition.
    
    Time Complexity: O(N) - linear scan through the partition
    Space Complexity: O(1) - constant space, in-place partitioning
    """
    pivot = customList[start]
    swap = start
    if stop - start > 1:
        for i in range(start+1, stop):
            if customList[i] < pivot:
                swap += 1
                customList[swap], customList[i] = customList[i], customList[swap] 
        customList[start], customList[swap] = customList[swap], customList[start]
    return swap

"""   
cList = np.random.random_integers(0, 100, 250)
print(cList)
insertSort(cList)
print(cList)

cList = np.random.random_integers(0, 100, 250)
print(cList)
print(bucketSort(cList))

cList = np.random.random_integers(0, 100, 20)
print(cList)
print(mergeSort(cList))

cList = np.random.random_integers(0, 100, 20)
print(cList)
print(quickSort(cList))
"""

cList = np.random.random_integers(0, 100, 20)
print(cList)
print(quickSort_iterative(cList))


