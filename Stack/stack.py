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
        
        Args:
            value: The value to push onto the stack.
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
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list:
            return False
        return True
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False
    
    def pop(self):
        if self.isEmpty():
            return
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.list[-1]
        
    def push(self, value):
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
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def isEmpty(self):
        if self.LinkedList.head:
            return False
        return True
    
    def __str__(self):
        return '\n'.join([str(x.value) for x in self.LinkedList])
    
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
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

    



    
        

        
