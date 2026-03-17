"""Circular Singly Linked List implementation module.

This module provides implementation of a Circular Singly Linked List where the
last node's next pointer points back to the first node, forming a circular structure.
Unlike regular linked lists, there is no null pointer at the end.

Key Features:
    - Circular structure (last node points to first node)
    - Efficient at both ends (can easily access first and last)
    - Automatic traversal returns to start after reaching end
    - Support for insertion and deletion at any position

Classes:
    Node: Represents a single node in the circular list
    CSLinkedList: The circular singly linked list container

Supported Operations:
    - append, prepend, insert: Add elements
    - pop, pop_first, remove: Delete elements  
    - get, set: Access and modify elements
    - traverse, search: Iterate and find elements
    - __str__: String representation
"""

class Node:
    def __init__(self, value):
        """Initialize a circular linked list node.
        
        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.next = None

class CSLinkedList():
    def __init__(self, value=None):
        """Initialize a circular singly linked list with optional initial value.
        
        Args:
            value: Optional initial value for the list (default: None for empty list).
        """
        if value is not None:
            node = Node(value)
            node.next = node
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.tail = None
            self.head = None
            self.next = self
            self.length = 0
    
    def append(self, value):
        """Add a value to the end of the circular list.
        
        Args:
            value: The value to append.
        
        Returns:
            int: The new length of the list.
        """
        node = Node(value)

        if self.length > 0:
            self.tail.next = node
            node.next = self.head
            self.tail = node
        
        else:
            self.tail = node
            self.head = node
            node.next = node
        
        self.length += 1
        return self.length

    def prepend(self, value):
        """Add a value to the beginning of the circular list.
        
        Args:
            value: The value to prepend.
        
        Returns:
            int: The new length of the list.
        """
        node = Node(value)

        if self.length == 0:
            self.append(value)
        else:
            self.tail.next = node
            node.next = self.head
            self.head = node
        self.length += 1
        return self.length

    def insert(self, value, index):
        """Insert a value at a specific index in the circular list.
        
        Args:
            value: The value to insert.
            index: The position to insert at.
        """
        if index == 0:
            self.prepend(value)
        elif index == -1 or index == self.length -1:
            self.append(value)
        elif -1 <= index < self.length:
            temp_node = self.head
            for i in range(index):                
                if i == index - 1:   
                    node = Node(value) 
                    node.next = temp_node.next
                    temp_node.next = node
                    self.length += 1
                else:
                    temp_node = temp_node.next
        else:
            raise Exception
    
    def traverse(self):
        """Traverse and print all values in the circular list.
        
        Prints each value on a separate line, stopping after one full cycle.
        """
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break
    
    def get(self, index):
        """Get the node at a specific index.
        
        Args:
            index: The position to retrieve.
        
        Returns:
            Node: The node at the specified index, or None if out of bounds.
        """
        if index == -1:
            current_node = self.tail
        elif 0 <= index < self.length:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
        else:
            current_node = None
        return current_node
    
    def set(self, value, index):
        """Set the value at a specific index.
        
        Args:
            value: The new value.
            index: The position to update.
        
        Returns:
            bool: True if successful, False otherwise.
        """
        node = self.get(index)
        if node is not None:
            node.value = value
            return True
        return False
    
    def pop_first(self):
        """Remove and return the first element from the list.
        
        Returns:
            Node: The removed node, or None if list is empty.
        """
        if self.length == 0:
            return None
        elif self.length == 1:
            node = self.head
            self.head = None
            self.tail = None
        else:
            node = self.head
            self.head = node.next
            self.tail.next = self.head
            node.next = None
            self.length -= 1
        return node
    
    def pop(self):
        """Remove and return the last element from the list.
        
        Returns:
            Node: The removed node, or None if list is empty.
        """
        if self.length == 0:
            return None
        elif self.length == 1:
            node = self.tail
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_node.next = self.tail.next
            node = self.tail
            self.tail = current_node
        self.length -= 1
        return node
    
    def remove(self, index):
        """Remove the node at a specific index.
        
        Args:
            index: The position to remove.
        
        Returns:
            Node: The removed node, or None/Exception if out of bounds.
        """
        if index == 0:
            return self.pop_first()
        elif index == -1 or index == self.length -1:
            return self.pop()
        elif 0 <= index < self.length:
            prev_node = self.get(index-1)
            node = prev_node.next
            prev_node.next = prev_node.next.next
            self.length -= 1
            return node
        else:
            raise Exception

    def search(self, value):
        """Search for a value in the circular list.
        
        Args:
            value: The value to search for.
        
        Returns:
            bool: True if found, False otherwise.
        """
        current = self.head
        for  i in range(self.length):
            if current.value == value:
                print(f'{value} is at location {i}')
                return True
            current = current.next
        print(f'{value} is not in the list')
        return False
        
    def __str__(self):
        """Return string representation of the circular list.
        
        Returns:
            str: Formatted string showing all values in the list.
        """
        result = '['
        current_node = self.head
        for i in range(self.length):
            if i != self.length-1:
                result += f'{current_node.value} -> '
            else:
                result += f'{current_node.value}]'
            current_node = current_node.next
        return result
    
    def delete_all(self):
        self.head.next = None
        #self.tail = None
        self.length = 0

    

CSLinkedList = CSLinkedList()
CSLinkedList.append(10)
CSLinkedList.append(20)
CSLinkedList.append(30)
print(CSLinkedList)
CSLinkedList.prepend(40)
print(CSLinkedList)
CSLinkedList.insert(23, 0)
CSLinkedList.insert(45, -1)
CSLinkedList.insert(90, 2)
print(CSLinkedList)
print(CSLinkedList)
CSLinkedList.search(55)
CSLinkedList.search(10)
print(CSLinkedList.get(4).value)
print(CSLinkedList.set(66666, 4))
print(CSLinkedList)
print(CSLinkedList.pop_first().value)
print(CSLinkedList)
print(CSLinkedList.pop().value)
print(CSLinkedList)
print(CSLinkedList.remove(-1).value)
print(CSLinkedList)
print(CSLinkedList.delete_all())
print(CSLinkedList)
