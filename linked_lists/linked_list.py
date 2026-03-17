"""
Singly Linked List implementation module.

This module provides a complete implementation of a Singly Linked List where each
node contains a value and reference to the next node.

Key Features:
    - Dynamic size (no fixed capacity)
    - O(1) insertion/deletion at head
    - Support for negative indices
    - Easy value traversal

Classes:
    Node: Represents a single node in the linked list
    LinkedList: The linked list container

Supported Operations:
    - append, prepend, insert: Add elements
    - pop, remove, delete_all: Remove elements
    - get, set_value, search: Access and find elements
    - __str__, transverse: Display and iterate

Time Complexity: Access O(N), Insert/Delete at head O(1), at end O(N)
"""

class Node:
    def __init__(self, value=None, next=None):
        """Initialize a linked list node.
        
        Args:
            value: The value to store in the node (default: None).
            next: Reference to the next node (default: None).
        """
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value=None):
        """Initialize a singly linked list with optional initial value.
        
        Args:
            value: Optional initial value to add to the list (default: None for empty list).
        """
        node = None
        self.length = 0
        if value is not None:
            node = Node(value)
            self.length = 1
        else:
            self.head = node
            self.tail = node
    
    def append(self, value):
        """Add a value to the end of the linked list.
        
        Args:
            value: The value to append.
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def prepend(self, value):
        """Add a value to the beginning of the linked list.
        
        Args:
            value: The value to prepend.
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head 
            self.head = node
        self.length += 1

    def insert(self, value, index):
        """Insert a value at a specific index in the linked list.
        
        Supports negative indexing. Supports boundary values (0, length, -1).
        
        Args:
            value: The value to insert.
            index: The position to insert at (0-indexed, supports negative indices).
        
        Raises:
            Exception: If index is not an integer or is out of bounds.
        """
        if not isinstance(index, int):
            raise Exception(f'{index} is not an integer index')

        if index == 0 or index == -1 - self.length:
            self.prepend(value)
        elif index == self.length or index == -1:
            self.append(value)
        elif 0 < index < self.length or -self.length <= index < 0:
            if index < 0:
                index = self.length + index  # Convert negative index to positive

            current_node = self.head
            new_node = Node(value)
            for i in range(index - 1):  # Stop at the node just before the insertion point
                current_node = current_node.next
            
            temp_node = current_node.next
            current_node.next = new_node
            new_node.next = temp_node
            self.length += 1
        else:
            raise Exception(f'{index} is out of bounds for a LinkedList with length {self.length}')
        
    def __str__(self):
        """Return string representation of the linked list.
        
        Returns:
            str: List values separated by ' -> '.
        """
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result 

    def transverse(self):
        """Traverse and print all values in the linked list.
        
        Prints each value on a separate line.
        """
        current = self.head
        while current:
            print(current.value)
            current = current.next 

    def search(self, value):
        """Search for a value in the linked list.
        
        Args:
            value: The value to search for.
        
        Returns:
            int: The index of the value if found, None otherwise.
        """
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return None

    def get(self, index):
        """Get the node at a specific index.
        
        Args:
            index: The position to retrieve (-1 for last node).
        
        Returns:
            Node: The node at the specified index, or None if out of bounds.
        """
        temp = 0
        current = self.head
        if index == -1:
            return self.tail
        while current:
            if temp == index:
                return current
            temp += 1
            current = current.next
        return None

    def set_value(self, index, value):
        """Set the value at a specific index.
        
        Args:
            index: The position to update.
            value: The new value.
        
        Returns:
            bool: True if successful, False if index out of bounds.
        """
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def pop(self):
        """Remove and return the first node from the linked list.
        
        Returns:
            Node: The removed node, or None if the list is empty.
        """
        node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.length == 0:
            pass
        else:
            self.head = self.head.next
            node.next = None
            self.length -= 1
        return node

    def remove(self, index):
        """Remove and return the node at a specific index.
        
        Args:
            index: The position to remove.
        
        Returns:
            Node: The removed node, or None if index is out of bounds.
        """
        if index == 0:
            return self.pop()

        current = self.get(index-1)
        if current:
            temp = current.next
            current.next = temp.next
            self.length -= 1
            return temp

    def delete_all(self):
        """Delete all nodes, leaving the list empty.
        
        Returns:
            None
        """
        self.head = None
        self.tail = None
        

linkedList = LinkedList()
linkedList.append(23)
linkedList.append(3)
linkedList.append(10)
linkedList.append(288)

print(linkedList)

linkedList.prepend(133)
print(linkedList)
linkedList.insert(0, 0)
print(linkedList)
#linkedList.insert(40,linkedList.length-76)
print(linkedList.length)

print(LinkedList().pop())

linkedList = LinkedList()
linkedList.append(23)
linkedList.append(3)
linkedList.append(10)
linkedList.append(288)
print(linkedList.remove(2).value)
print(LinkedList().remove(-1))

print(linkedList.delete_all())

        



