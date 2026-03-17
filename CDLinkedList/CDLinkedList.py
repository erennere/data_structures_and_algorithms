"""
Circular Doubly Linked List implementation module.

This module provides an implementation of a Circular Doubly Linked List where
the last node's next pointer points to the first node, and the first node's
previous pointer points to the last node, forming a circular structure.

Key Features:
    - Circular structure (no null pointers at ends)
    - Bidirectional traversal (forward and backward)
    - Efficient operations at both ends
    - Support for negative indexing

Classes:
    Node: Represents a node with value, next, and prev pointers
    CDLinkedList: The circular doubly linked list container

Supported Operations:
    - append, prepend, insert: Add elements
    - pop, pop_first, remove: Delete elements
    - get, set: Access and modify elements
    - iter_from_start, iter_from_end: Iterate in both directions

Ideal for: Applications needing efficient circular access patterns
"""

class Node():
    def __init__(self, value=None):
        self.next = None
        self.prev = None
        self.value = value
    def __str__(self):
        return str(self.value)

class CDLinkedList():
    

    def initialization(self, value):
        if not self.length == 0:
            raise Exception('The list is already initialized')
        node = Node(value)
        node.next = node
        node.prev = node
        self.tail = node
        self.head = node
        self.length = 1

    def __init__(self, value=None):
        from collections.abc import Iterable
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        elif isinstance(value, Iterable) and not isinstance(value, str):
            for index,item in enumerate(value):
                if index == 0:
                    self.initialization(item)
                else:
                    self.append(item)
        else:
            self.initialization(value)

    def _validate_index(self, index, insert=False):
        if isinstance(index, int):
            if index < 0:
                index += self.length
            if not insert:
                if index < 0 or index >= self.length:
                    raise IndexError("Index out of bounds.")
            else:
                if index < 0 or index > self.length:
                    raise IndexError("Index out of bounds.")
            return index
        else:
            raise IndexError("Index out of bounds.")

    def __len__(self):
        return self.length
    
    def __str__(self):
        result = '['
        current = self.head
        while current:
            if current != self.tail:
                result += f'{current.value} <-> '
            else:
                result += f'{current.value}'
                break
            current = current.next
        return result + ']'

    def append(self, value):
        if self.length == 0:
            self.initialization(value)
            return True
    
        node = Node(value)
        node.next = self.head
        node.prev = self.tail
        self.tail.next = node
        self.head.prev = node
        self.tail = node
        self.length += 1
        return True
    
    def prepend(self, value):
        if self.length == 0:
            self.initialization(value)
            return True
        
        node = Node(value)
        node.next = self.head
        node.prev = self.tail
        self.tail.next = node
        self.head.prev = node
        self.head = node
        self.length += 1
        return True
    
    def get(self, index):
        index = self._validate_index(index)
        if index == 0:
            return self.head
        elif index == self.length -1:
            return self.tail
        else:
            if self.length % 2 != 0:
                mid_index = self.length // 2
            else:
                mid_index = self.length // 2 - 1

            current_node = None
            if index <= mid_index:
                current_node = self.head
                for i in range(index):
                    current_node = current_node.next
            else:
                current_node = self.tail
                for i in range(self.length - index - 1):
                    current_node = current_node.prev
            return current_node
        
    def set(self, index, value):
        node = self.get(index)
        node.value = value
        return True

    def insert(self, index, value):
        index = self._validate_index(index, insert=True)
        
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            current_node = self.get(index)
            node = Node(value) 
            node.next = current_node
            node.prev = current_node.prev
            current_node.prev.next = node
            current_node.prev = node
            self.length += 1

    def pop(self):
        if self.length > 1:
            node = self.tail
            self.tail.prev.next = self.head
            self.head.prev = self.tail.prev
            self.tail = self.tail.prev
            node.prev = node.next = None
            self.length -= 1
            return node
        elif self.length == 1:
            node = self.head
            self.head = None
            self.tail = None
            node.next = node.prev = None
            self.length -= 1
            return node
        else:
            return None
        
    def pop_first(self):
        if self.length > 1:
            node = self.head
            self.head.next.prev = self.tail
            self.tail.next = self.head.next
            self.head = self.head.next
            node.prev = node.next = None
            self.length -= 1
            return node
        else:
            return self.pop()
        
    def remove(self, index):
        index = self._validate_index(index)
        if index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            node = self.get(index)
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = node.next = None
            self.length -= 1
            return node
        
    def iter_from_start(self):
        if self.length == 0:
            return
        
        current_node = self.head
        for _ in range(self.length):
            yield current_node
            current_node = current_node.next
    
    def iter_from_end(self):
        if self.length == 0:
            return
        
        current_node = self.tail
        for _ in range(self.length):
            yield current_node
            current_node = current_node.prev
        
    def __iter__(self):
        return self.iter_from_start()
    
    def search(self, value):
        if self.length:
            for index, current in enumerate(self):
                if current.value == value:
                    return index
        return -1
    
    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __getitem__(self, index):
        # Check if it's a slice
        if isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            # Handle negative indices by converting to positive
            if start is not None and start < 0:
                start += self.length
            if stop is not None and stop < 0:
                stop += self.length
            # Create a new list to store the sliced elements
            result = []
            current_node = self.head
            for i in range(self.length):
                if (start is None or i >= start) and (stop is None or i < stop):
                    result.append(current_node.value)
                current_node = current_node.next
            return result
        else:
            # Handle individual index
            return self.get(index).value

    def __setitem__(self, index, value):
        # Check if it's a slice
        if isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            # Handle negative indices by converting to positive
            if start is not None and start < 0:
                start += self.length
            if stop is not None and stop < 0:
                stop += self.length
            current_node = self.head
            for i in range(self.length):
                if (start is None or i >= start) and (stop is None or i < stop):
                    current_node.value = value
                current_node = current_node.next
        else:
            # Handle individual index
            node = self.get(index)
            node.value = value

    def concatenate(self, l2: "CDLinkedList") -> "CDLinkedList":
        if self.length > 0 and l2.length > 0:
            self.tail.next = l2.head
            l2.head.prev = self.tail
            l2.tail.next = self.head
            self.head.prev = l2.tail
            self.tail = l2.tail
            self.length += l2.length
        elif self.length == 0 and l2.length > 0:
            self.head = l2.head
            self.tail = l2.tail
            self.head.next = self.tail
            self.tail.prev = self.head
            self.length = l2.length
        return self
    
    def tolist(self):
        return [current.value for current in self]

# Test Script for CDLinkedList

def test_cdll():
    # Create an empty CDLinkedList
    cdll = CDLinkedList()
    
    print("=== Test 1: Empty List ===")
    
    # Test get and set on an empty list
    try:
        print("Getting value at index 0 on empty list:")
        cdll.get(0)
    except IndexError as e:
        print(f"Expected IndexError: {e}")

    try:
        print("Setting value at index 0 on empty list:")
        cdll.set(0, 100)
    except IndexError as e:
        print(f"Expected IndexError: {e}")
    
    # Test pop and pop_first on an empty list
    print("Popping on empty list:")
    node = cdll.pop()
    print(f"Popped value: {node}")  # Expected: None
    
    print("Popping first on empty list:")
    node = cdll.pop_first()
    print(f"Popped first value: {node}")  # Expected: None

    print("=== Test 2: Appending Elements ===")
    
    # Append an element and test getting and setting it
    cdll.append(10)
    print(f"List after appending 10: {cdll}")  # Expected: [10]
    print(f"Getting value at index 0: {cdll.get(0).value}")  # Expected: 10
    cdll.set(0, 20)
    print(f"List after setting index 0 to 20: {cdll}")  # Expected: [20]

    print("=== Test 3: Prepending Elements ===")
    
    # Prepend an element and test getting and setting it
    cdll.prepend(5)
    print(f"List after prepending 5: {cdll}")  # Expected: [5 <-> 20]
    print(f"Getting value at index 0: {cdll.get(0).value}")  # Expected: 5
    cdll.set(0, 15)
    print(f"List after setting index 0 to 15: {cdll}")  # Expected: [15 <-> 20]

    print("=== Test 4: Inserting Elements ===")
    
    # Test inserting at various positions
    cdll.insert(1, 10)
    print(f"List after inserting 10 at index 1: {cdll}")  # Expected: [15 <-> 10 <-> 20]
    
    try:
        print("Inserting at valid negative index -2 (should not raise exception):")
        cdll.insert(-2, 25)
        print(cdll)
    except IndexError as e:
        print(f"Expected IndexError: {e}")
    
    try:
        print("Inserting at invalid index 10 (should raise exception):")
        cdll.insert(10, 30)
    except IndexError as e:
        print(f"Expected IndexError: {e}")

    print("=== Test 5: Removing Elements ===")
    
    # Test removing elements at valid and invalid indices
    cdll.remove(1)
    print(f"List after removing node at index 1: {cdll}")  # Expected: [15 <-> 20]
    
    try:
        print("Removing at valid index -1 (should raise exception):")
        cdll.remove(-1)
        print(cdll)
    except IndexError as e:
        print(f"Expected IndexError: {e}")
    
    try:
        print("Removing at invalid index 10 (should raise exception):")
        cdll.remove(10)
    except IndexError as e:
        print(f"Expected IndexError: {e}")

    print("=== Test 6: Popping Elements ===")
    
    # Test popping elements from a list with multiple items
    node = cdll.pop()
    print(f"Popped value: {node.value}")  # Expected: 20
    print(f"List after pop: {cdll}")  # Expected: [15]

    node = cdll.pop_first()
    print(f"Popped first value: {node.value}")  # Expected: 15
    print(f"List after pop_first: {cdll}")  # Expected: []

    print("=== Test 7: Concatenating Lists ===")
    
    # Concatenate two non-empty lists
    cdll1 = CDLinkedList()
    cdll1.append(10)
    cdll1.append(20)
    cdll2 = CDLinkedList()
    cdll2.append(30)
    cdll2.append(40)
    print(f"List 1 before concatenation: {cdll1}")  # Expected: [10 <-> 20]
    print(f"List 2 before concatenation: {cdll2}")  # Expected: [30 <-> 40]
    cdll1.concatenate(cdll2)
    print(f"List 1 after concatenation: {cdll1}")  # Expected: [10 <-> 20 <-> 30 <-> 40]

    print("=== Test 8: Search Function ===")
    
    # Test searching for a value
    index = cdll1.search(30)
    print(f"Index of value 30: {index}")  # Expected: 2
    
    index = cdll1.search(100)
    print(f"Index of value 100: {index}")  # Expected: -1 (not found)

    print("=== Test 9: Iteration ===")
    
    # Test iteration from start
    print("Iterating from start:")
    for node in cdll1:
        print(node.value, end=" ")  # Expected: 10 20 30 40
    print()

    # Test iteration from end
    print("Iterating from end:")
    for node in cdll1.iter_from_end():
        print(node.value, end=" ")  # Expected: 40 30 20 10
    print()

    print("=== Test 10: Deleting All Elements ===")
    
    # Test deleting all elements
    cdll1.clear()
    print(f"List after deleting all elements: {cdll1}")  # Expected: []

    print("=== Test 11: Edge Case - Handling Empty List Operations ===")
    
    # Test append on an empty list
    cdll2 = CDLinkedList()
    cdll2.append(100)
    print(f"List after appending 100: {cdll2}")  # Expected: [100]
    
    # Test removing first element on a single-element list
    cdll2.pop_first()
    print(f"List after popping first: {cdll2}")  # Expected: []
    
    # Test pop on an empty list
    node = cdll2.pop()
    print(f"Pop on empty list result: {node}")  # Expected: None

    print("=== Test 12: Negative Indices ===")
    
    # Test negative indices for getting and setting elements
    cdll1.append(10)
    cdll1.append(20)
    cdll1.append(30)
    cdll1.append(40)
    
    print(f"List after appending 10, 20, 30, 40: {cdll1}")  # Expected: [10 <-> 20 <-> 30 <-> 40]
    
    print(f"Getting value at index -1: {cdll1.get(-1).value}")  # Expected: 40
    print(f"Getting value at index -2: {cdll1.get(-2).value}")  # Expected: 30
    print(f"Getting value at index -3: {cdll1.get(-3).value}")  # Expected: 20
    print(f"Getting value at index -4: {cdll1.get(-4).value}")  # Expected: 10

# Run the tests
test_cdll()

        
        

    



    

            

        

        
            

            



        

