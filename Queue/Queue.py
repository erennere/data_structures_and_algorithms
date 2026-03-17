"""
Queue data structure implementations module.

This module provides two implementations of Queue (FIFO - First In First Out):
1. Queue: Using a linked list for unbounded capacity
2. CapacityQueue: Using a fixed-size array with circular buffer

A Queue is a collection where elements are added at the rear and removed from
the front, following the First-In-First-Out principle.

Classes:
    Node: Represents a single node in the linked list
    LinkedList: Helper linked list for unbounded queue
    Queue: Queue implementation using linked list
    CapacityQueue: Queue with fixed maximum capacity

Supported Operations:
    - enqueue: Add element to rear
    - dequeue: Remove element from front
    - peek: View front element
    - isEmpty/isFull: Check queue status

Time Complexity: O(1) enqueue and dequeue operations
"""

class Node:
    def __init__(self, value):
        """Initialize a queue node.
        
        Args:
            value: The data to store in the node.
        """
        self.value = value
        self.next = None
    
class LinkedList():
    def __init__(self):
        """Initialize an empty linked list for queue operations."""
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        """Add a node to the end of the list.
        
        Args:
            value: The data to append.
        """
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop_first(self):
        """Remove and return the first node from the list.
        
        Returns:
            Node: The removed node, or None if the list is empty.
        """
        if self.length:
            node = self.head
            self.head = self.head.next
            self.length -= 1
            node.next = None
            return node
        return

class Queue():
    def __init__(self):
        """Initialize an empty queue using a linked list."""
        self.LinkedList = LinkedList()
    
    def enqueue(self, job):
        """Add an item to the back of the queue.
        
        Args:
            job: The data to enqueue.
        """
        self.LinkedList.append(job)
    
    def dequeue(self):
        """Remove and return the item from the front of the queue.
        
        Returns:
            The dequeued data, or None if the queue is empty.
        """
        if self.LinkedList.head:
            return self.LinkedList.pop_first().value
        return 
    
    def isEmpty(self):
        """Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise.
        """
        if self.LinkedList.head:
            return False
        return True
    
    def peek(self):
        """View the front item without removing it.
        
        Returns:
            The front item data, or None if the queue is empty.
        """
        if self.LinkedList.head:
            return self.LinkedList.head.value
        return
        
class CapacityQueue():
    def __init__(self, max_size):
        """Initialize a capacity-limited queue using circular array.
        
        Args:
            max_size (int): The maximum number of elements the queue can hold.
        """
        self.items = max_size*[None]
        self.max_size = max_size
        self.start = -1
        self.top = -1

    def __str__(self):
        """Return string representation of the queue.
        
        Returns:
            str: Space-separated string of all items.
        """
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        """Check if the queue is full.
        
        Returns:
            bool: True if queue has reached maximum capacity, False otherwise.
        """
        if self.top + 1 == self.max_size:
            if self.start == 0:
                return True
        elif self.start + 1 == self.top:
            return True
        return False

    def isEmpty(self):
        """Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise.
        """
        return self.start == self.top

    def enqueue(self, job):
        """Add an item to the back of the queue.
        
        Args:
            job: The data to enqueue.
        """
        if not self.isFull():
            if self.top + 1 < self.max_size:
                self.top += 1
                self.items[self.top] = job
            else:
                self.top = 0
                self.items[self.top] = job
                if self.start == -1:
                    self.start = 0
        else:
            print('The queue is full')

    def dequeue(self):
        """Remove and return the item from the front of the queue.
        
        Returns:
            The dequeued data, or None if the queue is empty.
        """
        if not self.isEmpty():
            temp = self.items[self.start]
            self.items[self.start] = None

            if self.start == self.head:
                self.head = self.start = -1
            
            else:
                if self.start + 1 == self.max_size:
                    self.start = 0
                else:
                    self.start += 1
            
            return temp
        
        else:
            print('The Queue is alreadzy empty!')
            return None

    def peek(self):
        """View the front item without removing it.
        
        Returns:
            The front item data, or None if the queue is empty.
        """
        if not self.isEmpty():
            return self.items[self.start]
        else:
            return None
