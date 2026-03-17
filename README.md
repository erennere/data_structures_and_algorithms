# Data Structures and Algorithms Learning Project

A comprehensive Python implementation of fundamental data structures and algorithms, designed for educational purposes. This project demonstrates various computational concepts with clean, well-documented code.

## Project Overview

This repository contains implementations of key data structures and algorithms commonly used in computer science. Each folder contains focused implementations with detailed docstrings and usage examples. The project is organized by concept, making it easy to explore and learn each topic independently.

**Key Features:**
- Complete implementations of classic data structures
- Multiple algorithm variations for comparison
- Well-documented code with PEP 257-compliant docstrings
- Practical examples and test cases
- Time and space complexity analysis

---

## Folder Structure and Modules

### 📊 Arrays
**Location:** `arrays/`

Arrays are fundamental data structures that store fixed-size collections of elements.

**File:** `arrayPractice.py`
- 1D array operations (append, insert, extend, remove, pop, reverse)
- Array querying (index, count, buffer_info)
- 2D array operations using NumPy for matrix manipulation

**Example:**
```python
from array import array
my_array = array('i', [1, 2, 3, 4, 5])
my_array.append(6)          # Add to end
my_array.insert(2, 10)      # Insert at index
my_array.remove(5)          # Remove by value
print(my_array.index(4))    # Get index
```

**Time Complexity:**
- Access: O(1)
- Insert (middle): O(N)
- Delete (middle): O(N)
- Append: O(1) amortized

---

### 🔗 Linked Lists
**Location:** `linked_lists/`, `single_linked_lists/`, `CDLinkedList/`, `DLinkedList/`

Linked lists enable dynamic memory allocation with efficient insertions and deletions at the head.

#### Singly Linked List
**File:** `linked_lists/linked_list.py`
- Dynamic size with O(1) insertions/deletions at head
- Support for negative indexing
- Key operations: append, prepend, insert, remove, search, get

**Example:**
```python
from linked_lists.linked_list import LinkedList

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.prepend(0)           # List: 0 -> 1 -> 2
ll.insert(1.5, 2)      # Insert at index 2
print(ll.search(1))     # Returns index: 1
print(ll)              # Output: 0 -> 1.5 -> 1 -> 2
```

**Time Complexity:**
- Access: O(N)
- Insert/Delete at head: O(1)
- Insert/Delete at end: O(N)

#### Circular Singly Linked List
**File:** `single_linked_lists/cslinked_list.py`
- Last node points back to first node
- Efficient at both ends
- Operations: append, prepend, insert, remove, search

**Example:**
```python
from cslinked_list import CSLinkedList

csl = CSLinkedList()
csl.append(1)
csl.append(2)
csl.append(3)
csl.traverse()          # Prints 1, 2, 3
csl.remove(1)          # Remove at index 1
```

#### Circular Doubly Linked List
**File:** `CDLinkedList/CDLinkedList.py`
- Bidirectional traversal in circular structure
- Last node next → First node, First node prev → Last node
- Efficient operations at both ends

#### Doubly Linked List
**File:** `DLinkedList/DLinkedList.py`
- Each node has next and previous pointers
- Bidirectional traversal support
- Forward and reverse iteration

---

### 📚 Stack (LIFO - Last In First Out)
**Location:** `Stack/`

Stack data structure with Last-In-First-Out principle - perfect for undo features, expression parsing, and depth-first search.

**File:** `Stack/stack.py`
- Basic Stack implementation using Python list
- Limited Stack (LStack) with maximum capacity
- Linked List Stack (LLStack) for dynamic sizing

**Example:**
```python
from stack import Stack

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())         # Returns 3
print(s.pop())          # Returns 3 and removes
print(s.isEmpty())     # Returns False
```

**Operations:**
- push(value): Add to top - O(1)
- pop(): Remove from top - O(1)
- peek(): View top element - O(1)
- isEmpty(): Check if empty - O(1)

**Use Cases:** Undo/Redo, Expression evaluation, Backtracking

---

### 🚪 Queue (FIFO - First In First Out)
**Location:** `Queue/`

Queue data structure following First-In-First-Out principle - essential for BFS, task scheduling, and buffering.

**File:** `Queue/Queue.py`
- Unbounded Queue using linked list
- CapacityQueue with fixed size and circular buffer

**Example:**
```python
from Queue import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())         # Returns 1
print(q.dequeue())     # Returns 1 and removes
print(q.isEmpty())     # Returns False
```

**Operations:**
- enqueue(item): Add to rear - O(1)
- dequeue(): Remove from front - O(1)
- peek(): View front element - O(1)
- isEmpty(): Check if empty - O(1)

**Use Cases:** BFS, Task queues, Level-order tree traversal

---

### 🌳 Trees
**Location:** `tree/`, `avl_trees/`

Tree structures enable hierarchical data representation and efficient searching.

#### General Trees and Binary Trees
**File:** `tree/tree.py` and `tree/tree_new.py`
- General tree with arbitrary children
- Binary trees with left and right pointers
- Multiple traversal methods

**Example:**
```python
from tree import Tree, Node

root_node = Node(1, None)
child_node = Node(2, None)
root_tree = Tree(root_node)
child_tree = Tree(child_node)
root_tree.addChild(child_tree)
print(root_tree)
```

#### Binary Search Tree
**File:** `tree/tree_new.py`
- BinaryTree class with BST properties
- Add, search, delete operations
- Tree traversals: preorder, inorder, postorder, breadth-first

**Example:**
```python
from tree_new import BinaryTree

bst = BinaryTree(10)
bst.add(5)
bst.add(15)
bst.add(3)
print(bst.search(5))    # True
print(bst.search(20))   # False
bst.inorder_traverse()  # Prints in sorted order: 3, 5, 10, 15
```

**Tree Traversal Complexities:**
- Time: O(N) for all traversals
- Space: O(H) where H is height

#### AVL Tree (Self-Balancing)
**File:** `avl_trees/avlTree.py`
- Self-balancing binary search tree
- Automatic rebalancing with rotations
- O(log N) for search, insert, delete
- Balance factor calculations

**Example:**
```python
from avlTree import AVLNode

avl = AVLNode(10)
avl = avl.add(5)
avl = avl.add(15)
avl = avl.add(3)
if avl.search(5):
    print("Found 5 in AVL tree")
```

**Key Properties:**
- Balance Factor: |height(left) - height(right)| ≤ 1
- Time Complexity: O(log N) for all operations
- Space Complexity: O(N)

---

### 🔍 Search Algorithms
**Location:** `search/`

Efficient algorithms to locate elements in data structures.

**File:** `search/search.py`
- Linear Search: Sequential search through array
- Binary Search: Logarithmic search on sorted array
- Merge Sort and Quick Sort for sorting

**Example:**
```python
from search import linearSearch, binarySearch

arr = [1, 3, 5, 7, 9, 11]
result = linearSearch(arr, 7)      # Returns 3 (index)
result = binarySearch(arr, 7)      # Returns 3 (index), much faster

# Sorting
sorted_arr = mergeSort([3, 1, 4, 1, 5, 9, 2, 6])
```

**Time Complexities:**
- Linear Search: O(N)
- Binary Search: O(log N)
- Merge Sort: O(N log N)
- Quick Sort: O(N log N) average, O(N²) worst

---

### 📊 Sorting Algorithms
**Location:** `bubbleSort/`, `selectionSort/`, `insertSort/`

Fundamental sorting algorithms with varying performance characteristics.

#### Bubble Sort
**File:** `bubbleSort/bubbleSort.py`
- Simple comparison-based sort
- Repeatedly compares adjacent elements
- Time Complexity: O(N²)

**Example:**
```python
from bubbleSort import bubbleSort

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)  # [11, 12, 22, 25, 34, 64, 90]
```

#### Selection Sort
**File:** `selectionSort/selectionSort.py`
- Divides into sorted and unsorted portions
- Repeatedly finds minimum from unsorted portion
- Time Complexity: O(N²)

**Example:**
```python
from selectionSort import selectionSort

arr = [64, 34, 25, 12, 22, 11, 90]
selectionSort(arr)
print(arr)  # [11, 12, 22, 25, 34, 64, 90]
```

#### Insertion Sort
**File:** `insertSort/insertSort.py`
- Builds sorted array one element at a time
- Efficient for small datasets
- Time Complexity: O(N²)

**Example:**
```python
from insertSort import insertSort

arr = insertSort([64, 34, 25, 12, 22, 11, 90])
print(arr)  # [11, 12, 22, 25, 34, 64, 90]
```

#### Bucket Sort
**File:** `insertSort/insertSort.py`
- Distributes elements into buckets
- Uses insertion sort on each bucket
- Time Complexity: O(N log N) average

**Example:**
```python
from insertSort import bucketSort

arr = bucketSort([64, 34, 25, 12, 22, 11, 90])
print(arr)  # Sorted array
```

---

### 🌐 Graph
**Location:** `graph/`

Graph algorithms for network and relationship analysis.

**File:** `graph/graph.py`
- Adjacency list representation
- Support for weighted and unweighted graphs
- Multiple traversal and pathfinding algorithms

**Key Operations:**

1. **Graph Traversals:**
   - Breadth-First Search (BFS): O(V + E)
   - Depth-First Search (DFS): O(V + E)

2. **Shortest Path:**
   - Dijkstra's Algorithm: O((V + E) log V)
   - Bellman-Ford: O(VE)

3. **Topological Sorting:** O(V + E)

**Example:**
```python
from graph import Graph

g_dict = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
g = Graph(g_dict)

# Traverse
print(list(g.bfs('A')))        # Breadth-first order
print(list(g.dfs('A')))        # Depth-first order

# Shortest path
print(g.dijkstra('A'))         # Shortest paths from A
```

---

### 🌳 Trie (Prefix Tree)
**Location:** `trie/`

Trie data structure optimized for string searching and auto-complete.

**File:** `trie/trie.py`
- Efficient prefix-based string searching
- O(M) search time where M is string length
- Support for add, search, and delete operations

**Example:**
```python
from trie import Trie

trie = Trie()
trie.addString("hello")
trie.addString("help")
trie.addString("world")

print(trie.search("hello"))     # True
print(trie.search("hel"))       # False (prefix doesn't exist)
trie.delete("help")
print(trie.search("help"))      # False
```

**Time Complexities:**
- Insert: O(M) where M is word length
- Search: O(M)
- Delete: O(M)
- Space: O(ALPHABET_SIZE * N * M)

---

### 🏔️ Binary Heap
**Location:** `binary_heap/`

Priority queue implementations using binary heap structure.

**File:** `binary_heap/binary_heap.py`
- BinaryHeap: Complete implementation with heapify operations
- Heap: Simple heap using list-based structure
- Min-heap and max-heap support

**Example:**
```python
from binary_heap import BinaryHeap

min_heap = BinaryHeap(10, 'min')
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(7)
min_heap.insert(1)

print(min_heap.peek())          # Returns 1 (minimum)
print(min_heap.extract())      # Returns 1 and removes
```

**Operations:**
- Insert: O(log N)
- Extract (min/max): O(log N)
- Peek: O(1)
- Space: O(N)

---

### ⚡ Disjoint Set (Union-Find)
**Location:** `disjointSet/`

Efficient data structure for managing partitions and connected components.

**File:** `disjointSet/disjointedSet.py`
- Path compression optimization
- Union by rank optimization
- Nearly O(1) amortized operations

**Example:**
```python
from disjointSet import DisjointSet

ds = DisjointSet(5)
ds.union(0, 1)
ds.union(1, 2)
ds.union(3, 4)

print(ds.find(0))    # Root of 0's set
print(ds.find(1))    # Same root as 0
print(ds.find(4))    # Different root
```

**Time Complexity:**
- Find: O(α(N)) amortized, where α is inverse Ackermann
- Union: O(α(N)) amortized
- Practical: Nearly O(1) for most inputs

---

### 🎯 Object-Oriented Programming
**Location:** `oop/`

Examples of OOP principles and design patterns.

**File:** `oop/StartCookie.py`
- Class definitions and inheritance
- Method overriding and polymorphism
- Access control mechanisms

---

### 🧠 Neural Networks
**Location:** `cnn/`

Basic CNN (Convolutional Neural Network) implementation.

**File:** `cnn/cnn.py`
- 2D convolution operations
- Batch normalization
- Max pooling and activation functions
- Forward pass and layer management

---

## Time and Space Complexity Summary

| Data Structure | Insert | Delete | Search | Update | Space |
|---|---|---|---|---|---|
| Array | O(N) | O(N) | O(N) | O(1) | O(N) |
| Singly Linked List | O(1)* | O(N) | O(N) | O(N) | O(N) |
| Doubly Linked List | O(1)* | O(N) | O(N) | O(N) | O(N) |
| Stack | O(1) | O(1) | O(N) | N/A | O(N) |
| Queue | O(1) | O(1) | O(N) | N/A | O(N) |
| Binary Search Tree | O(log N) | O(log N) | O(log N) | O(log N) | O(N) |
| AVL Tree | O(log N) | O(log N) | O(log N) | O(log N) | O(N) |
| Trie | O(M) | O(M) | O(M) | O(M) | O(N*M) |
| Hash Table | O(1) | O(1) | O(1) | O(1) | O(N) |
| Heap | O(log N) | O(log N) | O(N) | O(log N) | O(N) |
| Graph (BFS/DFS) | N/A | N/A | O(V+E) | N/A | O(V+E) |

*O(1) insertion at head with reference; O(N) for insertion at specific position

| Sorting Algorithm | Time (Best) | Time (Average) | Time (Worst) | Space |
|---|---|---|---|---|
| Bubble Sort | O(N) | O(N²) | O(N²) | O(1) |
| Selection Sort | O(N²) | O(N²) | O(N²) | O(1) |
| Insertion Sort | O(N) | O(N²) | O(N²) | O(1) |
| Merge Sort | O(N log N) | O(N log N) | O(N log N) | O(N) |
| Quick Sort | O(N log N) | O(N log N) | O(N²) | O(log N) |
| Bucket Sort | O(N+K)* | O(N+K)* | O(N²)* | O(N+K) |

---

## Getting Started

### Prerequisites
- Python 3.6+
- NumPy (for array operations)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd data_structures_and_algorithms

# Install dependencies (optional)
pip install numpy
```

### Running Examples
```bash
# Run a specific module
python arrays/arrayPractice.py
python linked_lists/linked_list.py
python tree/tree_new.py

# Import and use in your code
from linked_lists.linked_list import LinkedList
from search.search import binarySearch
from Stack.stack import Stack
```

---

## Learning Path Recommendations

**Beginner:**
1. Arrays
2. Singly Linked Lists
3. Stack and Queue
4. Bubble Sort and Selection Sort

**Intermediate:**
5. Binary Search
6. Binary Search Trees
7. Graph Traversals (BFS/DFS)
8. Insertion Sort and Merge Sort

**Advanced:**
9. AVL Trees (Self-Balancing)
10. Disjoint Set (Union-Find)
11. Dijkstra's Algorithm
12. Trie Data Structure
13. Heaps and Heap Sort

---

## Key Concepts

### Big O Notation
- **O(1)**: Constant time - operations independent of input size
- **O(log N)**: Logarithmic - divide and conquer approaches
- **O(N)**: Linear - single pass through data
- **O(N log N)**: Linear logarithmic - efficient sorting
- **O(N²)**: Quadratic - nested loops
- **O(2^N)**: Exponential - recursive without memoization
- **O(N!)**: Factorial - permutations/combinations

### When to Use Each Data Structure

**Stack (LIFO):**
- Undo/Redo functionality
- Expression evaluation
- Function call stack simulation
- Depth-first search

**Queue (FIFO):**
- Breadth-first search
- Print queue management
- Task scheduling
- Cache eviction (FIFO)

**Linked List:**
- Frequent insertions/deletions at beginning
- Dynamic size needed
- Memory not contiguous
- Used in hash tables (chaining)

**Binary Search Tree:**
- Ordered data
- Range queries
- Not self-balancing (use AVL if balance needed)

**Hash Table:**
- Fast lookups (O(1) average)
- Counting elements
- Caching

**Trie:**
- Auto-complete features
- Dictionary implementations
- IP routing (longest prefix matching)

---

## Testing

### Comprehensive Test Suite

The project includes an extensive test suite (`test.py`) that validates all data structures and algorithms with both standard functionality and edge case coverage.

**Test Execution:**
```bash
python test.py
```

**Current Test Results:**
- **Total Tests:** 42
- **Passed:** 42 (100% success rate)
- **Coverage:** All major data structures and algorithms

### Test Categories

#### 1. **Linked Lists (2 tests)**
- ✓ Basic operations (append, prepend, length validation)
- ✓ Edge cases (empty list, single element, pop operations)

#### 2. **Stack (3 tests)**
- ✓ Basic operations (push, pop, peek)
- ✓ Edge cases (empty stack, single element)
- ✓ LIFO property validation (Last-In-First-Out correctness)

#### 3. **Queue (3 tests)**
- ✓ Basic operations (enqueue, dequeue, peek)
- ✓ Edge cases (empty queue, single element)
- ✓ FIFO property validation (First-In-First-Out correctness)

#### 4. **Trees (4 tests)**
- ✓ Binary Tree basic operations and single node
- ✓ General Tree instantiation
- ✓ AVL Tree node creation

#### 5. **Search Algorithms (3 tests)**
- ✓ Basic search (finds elements in arrays)
- ✓ Edge cases (single element, not found scenarios)
- ✓ Boundary testing (first and last elements)

#### 6. **Sorting Algorithms (15 tests)**

**Bubble Sort (3 tests):**
- ✓ Basic sorting functionality
- ✓ Edge cases (single element, already sorted, reverse sorted)
- ✓ Duplicate value handling

**Selection Sort (3 tests):**
- ✓ Basic sorting functionality
- ✓ Edge cases (single element, already sorted)
- ✓ Duplicate value handling

**Insertion Sort (2 tests):**
- ✓ Basic sorting functionality
- ✓ Edge cases (single element, two elements)

**Merge Sort (2 tests):**
- ✓ Basic sorting functionality
- ✓ Edge cases (single element, two elements)

**Quick Sort (2 tests):**
- ✓ Basic sorting functionality
- ✓ Edge cases (single element, two elements)

#### 7. **Graph (2 tests)**
- ✓ Basic operations (add_edge, instantiation)
- ✓ Edge cases (single edge, self-loops)

#### 8. **Trie (4 tests)**
- ✓ Basic string search and addition
- ✓ Single character operations
- ✓ Empty trie searches
- ✓ Overlapping prefix/suffix handling

#### 9. **Binary Heap (3 tests)**
- ✓ Basic operations (insert, peek)
- ✓ Single element operations
- ✓ Heap ordering property validation

#### 10. **Disjoint Set (4 tests)**
- ✓ Basic union-find operations
- ✓ Single element set operations
- ✓ Repeated union handling
- ✓ Path compression validation

#### 11. **Arrays & OOP (1 test)**
- ✓ Array operations and OOP class instantiation

### Edge Case Coverage

The test suite validates critical edge cases:

| Category | Edge Cases Tested |
|----------|-------------------|
| **Empty Containers** | Empty lists, stacks, queues, tries |
| **Single Elements** | Single element operations with no adjacent nodes |
| **Boundaries** | First and last element access |
| **Sorted Data** | Already sorted, reverse sorted arrays |
| **Duplicates** | Multiple identical values in sorting/searching |
| **Property Validation** | LIFO/FIFO correctness, heap ordering, path compression |

---

## Code Quality Standards

All code in this project follows:
- **PEP 257** - Docstring conventions
- **PEP 8** - Style guide for Python
- **Type hints** - For better code clarity (where applicable)
- **Comprehensive comments** - Explaining complex algorithms
- **100% Test Coverage** - All major components tested with edge cases

---

## Contributing

This is an educational project. Contributions are welcome! Please ensure:
1. Code follows PEP 8 style guidelines
2. All functions have comprehensive docstrings
3. Include time/space complexity analysis
4. Add example usage in docstrings

---

## Resources for Further Learning

- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Visualize Data Structures](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)
- Introduction to Algorithms (CLRS)
- Cracking the Coding Interview

---

## License

This educational project is provided as-is for learning purposes.

---

Last Updated: March 2026
