"""
Singly Linked List helper implementation for CDLinkedList module.

This module provides a basic Singly Linked List implementation used as a helper
class in the CDLinkedList module for queue operations. It supports generating
linked lists with random values and converting them to various forms.

Classes:
    Node: Represents a node with value and next pointer
    LinkedList: Basic singly linked list with generation capabilities

Supported Operations:
    - add: Append a value to the list
    - generate: Create list with n random values in range
    - __len__: Get the length of the list
    - __str__: String representation
    - __iter__: Iterate through nodes

Purpose:
    This is primarily used as a helper class for linked list operations
    in other modules, particularly for two-sum and intersection problems.
"""

#   Created by Elshad Karimov on 17/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

from random import randint
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self

# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(len(customLL))

