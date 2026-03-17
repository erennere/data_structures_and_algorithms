"""
Stack implementations module.

This module provides three implementations of the Stack data structure:
1. Stack: Basic stack using a Python list
2. LStack: Limited-size stack with maximum capacity constraints
3. LLStack: Stack implemented using a singly linked list

Stack follows Last-In-First-Out (LIFO) principle where the last element
added is the first one to be removed.

Classes:
    Stack: Basic stack implementation
    LStack: Stack with maximum size limit
    Node: Helper node class for linked list operations
    LinkedList: Helper linked list class
    LLStack: Stack implemented using linked list
"""

class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self):
        """Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise.
        """
        if self.list:
            return False
        return True

    def push(self, value):
        """Push a value onto the top of the stack.
        
        Stack insertion is achieved by adding the new value to the top of the stack
        (end of the list). This maintains LIFO principle where the most recently added
        element will be the first one removed, making access from one end (top) efficient.
        
        Args:
            value: The value to push onto the stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            return
        else:
            return self.list.pop()
        
    def peek(self):
        """Return the top element without removing it.
        
        Returns:
            The top element if stack is not empty, None otherwise.
        """
        if self.isEmpty():
            return
        else:
            return self.list[-1]
        
    def clear(self):
        """Clear all elements from the stack."""
        self.list = None

class LStack():
    """Limited-capacity stack implementation using a Python list.
    
    A stack with a maximum size limit. All operations maintain LIFO (Last-In-First-Out)
    principle: elements are pushed to the top and popped from the top. The stack prevents
    adding more elements than the specified maximum capacity.
    
    Attributes:
        maxSize (int): Maximum number of elements the stack can hold.
        list (list): Internal list containing stack elements.
    """
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self):
        """Check if the stack is empty.
        
        Emptiness is determined by whether the internal list contains any elements.
        Useful before calling pop() to avoid returning None unexpectedly.
        
        Returns:
            bool: True if stack is empty, False otherwise.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.list:
            return False
        return True
    
    def isFull(self):
        """Check if the stack is at maximum capacity.
        
        Capacity is checked by comparing current size against maxSize. Useful before
        calling push() to prevent exceeding the maximum capacity constraint.
        
        Returns:
            bool: True if stack is full (size == maxSize), False otherwise.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if len(self.list) == self.maxSize:
            return True
    
    def pop(self):
        """Remove and return the top element from the limited stack.
        
        Stack removal is achieved by removing the most recently added element from
        the top, maintaining LIFO principle. Returns None if stack is empty.
        
        Returns:
            The element at the top of the stack, or None if stack is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.isEmpty():
            return
        else:
            return self.list.pop()
        
    def peek(self):
        """View the top element without removing it.
        
        Inspecting the top element is achieved by accessing the last element of the
        list without modifying the stack. Useful for checking what will be popped next.
        
        Returns:
            The element at the top of the stack, or None if stack is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.isEmpty():
            return
        else:
            return self.list[-1]
        
    def push(self, value):
        """Push a value onto the limited stack.
        
        Stack insertion is achieved by adding the new value to the top of the stack
        (end of the list), maintaining LIFO principle. Note: This implementation should
        check isFull() before pushing to respect capacity limits.
        
        Args:
            value: The value to push onto the stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.isEmpty:
            return
        else:
            self.list.append(value)

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class LLStack:
    """Stack implementation using a singly linked list.
    
    A stack built on a linked list structure where each element (node) points to the
    next element. All operations maintain LIFO (Last-In-First-Out) principle: elements
    are inserted/removed from the top of the stack. Using a linked list avoids
    reallocation issues of array-based stacks.
    
    Attributes:
        LinkedList (LinkedList): Internal linked list containing stack elements.
    """
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def isEmpty(self):
        """Check if the stack is empty.
        
        Emptiness is determined by whether the head of the linked list is None.
        A None head indicates no elements are in the stack.
        
        Returns:
            bool: True if stack is empty, False otherwise.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.LinkedList.head:
            return False
        return True
    
    def __str__(self):
        """Return string representation of the stack.
        
        Returns each element's value on a separate line, from top to bottom.
        
        Returns:
            str: String representation of the stack elements.
        """
        return '\n'.join([str(x.value) for x in self.LinkedList])
    
    def push(self, value):
        """Push a value onto the stack.
        
        Stack insertion is achieved by creating a new node and making it the new head
        of the linked list, with the previous head becoming its next node. This 
        maintains LIFO principle where the most recently added element (new head)
        is always at the top of the stack.
        
        Args:
            value: The value to push onto the stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        """Remove and return the top element from the stack.
        
        Stack removal is achieved by getting the head node and updating the head
        to point to the next node in the linked list. This removes the most recently
        added element (top), maintaining LIFO principle. Returns None if stack is empty.
        
        Returns:
            Node: The node at the top of the stack, or None if stack is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.isEmpty():
           node = self.LinkedList.head
           self.LinkedList.head = node.next
           return node
        return
    
    def peek(self):
        """View the top element without removing it.
        
        Returns:
            Node: The node at the top of the stack, or None if empty.
        """
        return self.LinkedList.head
    
    def clear(self):
        """Remove all elements from the stack."""
        self.LinkedList.head = None
    
llstack = LLStack()
print(llstack)
llstack.push(1)
llstack.push(2)
llstack.push(3)
llstack.push(4)
print(llstack.pop())
print(llstack)

    



    
        

        
