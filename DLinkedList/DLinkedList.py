"""
Doubly Linked List implementation module.

This module provides an implementation of a Doubly Linked List where each node
has references to both its next and previous nodes, allowing efficient traversal
in both directions.

Key Features:
    - Bidirectional traversal (forward and backward)
    - O(1) insertion/deletion at any position (with node reference)
    - Index-based access with optimization (faster from either end)
    - Support for negative indices

Classes:
    Node: Represents a single node in the doubly linked list
    DLinkedList: The doubly linked list container

Supported Operations:
    - append, prepend, insert: Add elements
    - pop, pop_first, remove: Delete elements
    - get, set: Access and modify elements
    - traverse, reverse_traverse: Iterate in both directions

Time Complexity: Most operations O(N) except insertion/deletion O(1) if node reference is known.
"""

class Node(object):
    def __init__(self, value=None):
        self.next = None
        self.prev = None
        self.value = value

    def __str__(self):
        return str(self.value)

class DLinkedList(object):
    def initialization(self, value):
        node = Node(value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        self.length = 1
        return True
    
    def _validate_index(self, index):
        if (index != -1 and index < 0) or index >= self.length:
            raise IndexError("Index out of bounds.")
    
    def __init__(self, value=None):
        if value:
            self.initialization(value)
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def __str__(self):
        current = self.head
        result = '['
        while current is not None:
            if current != self.tail:
                result += f'{current.value} <-> '
            else:
                result += f'{current.value}'
            current = current.next
        result += ']'
        return result
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def append(self, value):
        if self.length == 0:
            return self.initialization(value)
        else:    
            node = Node(value)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.length += 1
            return True

    def prepend(self, value):
        if self.length == 0:
            return self.initialization(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.length += 1
            return True

    def traverse(self):
        current = self.head
        while current is not None:
            print(current)
            current = current.next

    def reverse_traverse(self):
        current = self.tail
        while current is not None:
            print(current) 
            current = current.prev

    def search(self, value):
        current = self.head
        i = 0
        while current is not None:
            if current.value == value:
                print(f'{value} found at index {i}')
                return i
            current = current.next
            i += 1
        return -1
    
    def get(self, index):
        self._validate_index(index)

        if index == -1:
            return self.tail
        
        mid = self.length // 2
        if index >= mid:
            current = self.tail
            for _ in range(int(self.length - index - 1)):
                current = current.prev
            return current                
        if index < mid:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
        return None
    
    def set(self, index, value):
        self._validate_index(index)
        if self.length == 0:
            return False
        
        node = self.get(index)
        if node:
            node.value = value
        return True

    def insert(self, index, value):
        self._validate_index(index)
        if index == 0:
            return self.prepend(value)
        elif index == -1 or index == self.length -1:
            return self.append(value)
        elif index < 0:
            return False
        else:
            node = Node(value)
            current_node = self.get(index)
            current_node.prev.next = node
            node.prev = current_node.prev
            current_node.prev = node
            node.next = current_node
            self.length += 1
            return True
        
    def pop_first(self):
        if self.length == 0:
            return
        if self.length == 1:
            node = self.head
            self.head = self.tail = None
            node.prev = node.next = None
            self.length -= 1
            return node
        else:
            node = self.head
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            return node
        
    def pop(self):
        if self.length == 0:
            return
        if self.length == 1:
            node = self.tail
            self.head = self.tail = None
            node.prev = node.next = None
            self.length -= 1
            return node
        else:
            node = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
            return node
    
    def remove(self, index):
        self._validate_index(index)
        if index == 0:
            return self.pop_first()
        if index == -1 or index == self.length - 1:
            return self.pop()   
        else:
            node = self.get(index)
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = node.prev = None
            self.length -= 1
            return node
        
    def delete_all(self):
        self.head.next = None
        self.tail.prev = None
        self.head = self.tail = None      

dl = DLinkedList()
print(dl)
dl.append(10)
print(dl)
dl.prepend(20)
print(dl)
dl.append(34)
dl.append(56)
dl.append(76)
#dl.append(89)
print(dl)
print(dl.get(2))
dl.insert(3, 8888)
print(dl)
print(dl.pop_first())
print(dl)
print(dl.pop())
print(dl)
print(dl.remove(2))
print(dl)
print(dl.delete_all())
print(dl)

    

        
        
    

