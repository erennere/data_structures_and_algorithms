"""
Binary Heap implementations module.

This module provides two implementations of Binary Heap data structures:
1. BinaryHeap: A complete implementation with heapify operations
2. Heap: A basic heap implementation with push and insertion methods

A binary heap is a complete binary tree where each parent node is either
greater than (max heap) or less than (min heap) its children.

Classes:
    BinaryHeap: Complete binary heap with insert, extract, peek operations
    Heap: Basic heap implementation with insertion and heapify-up

Supported Operations:
    - Insert: Add elements while maintaining heap property
    - Extract: Remove and return root element
    - Peek: View root element without removing it
    - Traverse: Level-order traversal of heap elements
"""

class BinaryHeap:
    def __init__(self, size, heapType='min'):
        """Initialize a binary heap with specified size and type.
        
        Args:
            size (int): The maximum capacity of the heap.
            heapType (str): Type of heap - 'min' for min-heap, 'max' for max-heap (default: 'min').
        """
        self.size = size
        self.data = [None] * (self.size + 1)
        self.count = 0
        self.heapType = heapType
    
    
    def levelOrderTraversal(self):
        """Perform and print level-order traversal of the heap.
        
        Traversal is achieved by processing heap elements by their array indices
        from 1 to count, which naturally visits nodes level-by-level in the complete
        binary tree representation. This displays all elements currently in the heap.
        
        Time Complexity: O(N) where N is the number of elements
        Space Complexity: O(1)
        """
        if not self.data:
            return
        else:
            for i in range(1, self.count + 1):
                print(self.data[i])
    
    def peek(self):
        """Get the root element without removing it.
        
        Peeking is achieved by accessing the element at index 1, which is always the
        root of the complete binary tree representation. For min-heaps, this is the
        minimum element; for max-heaps, the maximum. Returns None if heap is empty.
        
        Returns:
            The root element (minimum for min-heap, maximum for max-heap), or None if empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.count == 0:
            return None
        return self.data[1]
    
    def _heapifyUp(self, index, heapType):
        """Move an element up the heap until heap property is restored.
        
        Heapifying up is achieved by comparing the element with its parent and
        swapping if they violate the heap property (for min-heap: child < parent,
        for max-heap: child > parent). This process repeats at each level up until
        reaching the correct position, restoring the heap property after insertion.
        
        Args:
            index (int): The index of the element to move up.
            heapType (str): Type of heap to determine comparison direction.
        
        Time Complexity: O(log N) where N is the number of elements
        Space Complexity: O(1)
        """
        while index > 1:
            parent_index = index // 2
            parent_value = self.data[parent_index]
            value =  self.data[index]
            if heapType == 'min':
                    if parent_value > value:
                        self.data[parent_index] = value
                        self.data[index] = parent_value
                        index = parent_index
                    else:
                        break
            elif heapType == 'max':
                    if parent_value < value:
                        self.data[parent_index] = value
                        self.data[index] = parent_value
                        index = parent_index
                    else:
                        break
    
    def insert(self, value):
        """Insert a value into the heap while maintaining heap property.
        
        Args:
            value: The value to insert.
        
        Raises:
            Exception: If the heap is full.
        """
        if self.count >= self.size:
            raise Exception('Heap is full!')
        self.count += 1
        self.data[self.count] = value
        self._heapifyUp(self.count, self.heapType)

    def extract(self):
        """Remove and return the root element from the heap.
        
        Returns:
            The root element (minimum for min-heap, maximum for max-heap), or None if empty.
        """
        if self.data:
            first_element = self.data[1]
            last_element = self.data[self.count]
            self.data[1] = last_element
            self.data[self.count] = None
            self.count -= 1
            self._heapifyDown(self.heapType)
            return first_element
        else:
            return

    def _heapifyDown(self, heapType):
        """Move an element down the heap until heap property is restored.
        
        Used after extraction to maintain heap property.
        
        Args:
            heapType (str): Type of heap to determine comparison direction.
        """
        index = 1
        while index*2 <= self.count:
            left =  2*index 
            right = 2*index + 1
            child_index = left

            if right <= self.count:
                if heapType == 'min' and self.data[right] < self.data[left]:
                    child_index = right
                if  heapType == 'max' and self.data[right] > self.data[left]:
                    child_index = right

            child_value = self.data[child_index]
            value = self.data[index]
            if heapType == 'min':
                if value > child_value:
                    self.data[child_index] = value
                    self.data[index] = child_value
                    index = child_index
                else:
                    break
            elif heapType == 'max':
                if value < child_value:
                    self.data[child_index] = value
                    self.data[index] = child_value
                    index = child_index
                else:
                    break


class Heap:
    def __init__(self, size, heap_type='min'):
        """Initialize a simple heap with specified size and type.
        
        Args:
            size (int): The maximum capacity of the heap.
            heap_type (str): Type of heap - 'min' for min-heap, 'max' for max-heap (default: 'min').
        """
        self.size = size
        self.heap_type = heap_type
        self.heap = [None]*(size)
        self.count = 0
    
    def insert(self, data):
        """Insert a value into the heap while maintaining heap property.
        
        Args:
            data: The value to insert.
        
        Returns:
            bool/None: Result of heapify-up operation.
        
        Raises:
            Exception: If the heap is full.
        """
        if self.count == self.size:
            raise Exception("Heap is Full!")
        self.heap[self.count] = data
        val = self._heapifyUp(self.count)
        self.count += 1
        return val 

    def _heapifyUp(self, index):
        """Move an element up the heap until heap property is restored.
        
        Args:
            index (int): The index of the element to move up.
        
        Returns:
            bool: True if heapification completed successfully.
        """
        if index == 0:
            return True
        parent_index = (index-1)//2
        if self.heap_type == 'min':
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                self._heapifyUp(parent_index)
            else:
                return True
        elif self.heap_type == 'max':
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                self._heapifyUp(parent_index)
            else:
                return True
            
    def pop(self):
        """Remove and return the root element from the heap.
        
        Returns:
            The root element (minimum for min-heap, maximum for max-heap), or None if empty.
        """
        if self.heap:
            data = self.heap[0]
            self.heap[0] = self.heap[self.count-1]
            self.heap[self.count-1] = None
            self.count -= 1
            self._heapifyDown()
            return data
        else:
            raise Exception('No data in the heap')

    def _heapifyDown(self, index=0):
        left_index = 2*index + 1
        right_index = 2*index + 2

        if self.heap_type == 'min':
            child_index = left_index if left_index < self.count else None
            if right_index < self.count and self.heap[right_index] < self.heap[child_index]:
                child_index = right_index

            if child_index is not None and self.heap[child_index] < self.heap[index]:
                self.heap[index], self.heap[child_index] = self.heap[child_index], self.heap[index]
                return self._heapifyDown(child_index)
            
            return True
        
        elif self.heap_type == 'max':
            child_index = left_index if left_index < self.count else None
            if right_index < self.count and self.heap[right_index] > self.heap[child_index]:
                child_index = right_index

            if child_index is not None and self.heap[child_index] > self.heap[index]:
                self.heap[index], self.heap[child_index] = self.heap[child_index], self.heap[index]
                return self._heapifyDown(child_index)
            return True
    
    def heapSort(self):
        org_count = self.count
        end = org_count - 1
        while end > 0:
            self.heap[0], self.heap[end] = self.heap[end], self.heap[0]
            self.count -= 1
            end -= 1
            self._heapifyDown()
        self.count = org_count

        if self.heap_type == 'min':
            self.heap[:org_count] = reversed(self.heap[:org_count])


import numpy as np
random_list = np.random.randint(1, 100, 44)
my_heap = Heap(len(random_list))
for i in random_list:
    my_heap.insert(int(i))

print(random_list)
print(my_heap.heap)
my_heap.heapSort()
print(my_heap.heap)

        






        
        
            
        


        
        

        
    
        



    
        

    