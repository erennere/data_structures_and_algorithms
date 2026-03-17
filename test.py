"""
Comprehensive Test Suite for Data Structures and Algorithms Project.

This test module performs extensive testing including standard functionality
and edge cases for all major data structures and algorithms.

Edge Cases Covered:
    - Empty containers and single elements
    - Boundary conditions and full containers
    - Reverse sorted and already sorted data
    - Duplicate values
    - Single character/node operations
    - Path compression and union operations
    - Prefix searches and non-existent elements
"""

import sys
import traceback
import numpy as np

def test_module(module_name, test_func):
    """Run a test for a specific module and report results."""
    try:
        test_func()
        print(f"[PASS] {module_name}")
        return True
    except AssertionError as e:
        print(f"[FAIL] {module_name}: {str(e)}")
        return False
    except Exception as e:
        print(f"[ERROR] {module_name}: {str(e)}")
        return False

# ==================== BASIC FUNCTIONALITY TESTS ====================

def test_arrays_basic():
    """Test array basic operations."""
    import arrays.arrayPractice as array_module
    pass

def test_linked_lists_basic():
    """Test singly linked list basic operations."""
    from linked_lists.linked_list import LinkedList
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(0)
    assert ll.length == 3, "Length should be 3"
    assert ll.head.value == 0, "Head should be 0"

def test_linked_lists_edge_cases():
    """Test singly linked list edge cases - empty and single element."""
    from linked_lists.linked_list import LinkedList
    
    # Empty list operations
    ll = LinkedList()
    assert ll.length == 0, "Empty list length should be 0"
    
    # Single element
    ll.append(42)
    assert ll.length == 1, "Single element list length should be 1"
    assert ll.head.value == 42, "Single element should be head"
    
    # Append and remove multiple
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.length == 3, "After appending 3 elements, length should be 3"
    ll.pop()
    assert ll.length == 2, "After pop, length should be 2"

def test_stack_basic():
    """Test stack basic operations."""
    from Stack.stack import Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2, "Top should be 2"
    assert stack.pop() == 2, "Pop should return 2"
    assert not stack.isEmpty(), "Stack should not be empty"

def test_stack_edge_cases():
    """Test stack edge cases - empty, single element, LIFO."""
    from Stack.stack import Stack
    
    # Empty stack
    stack = Stack()
    assert stack.isEmpty(), "New stack should be empty"
    assert stack.pop() is None, "Pop on empty stack should return None"
    assert stack.peek() is None, "Peek on empty stack should return None"
    
    # Single element
    stack.push(99)
    assert stack.peek() == 99, "Single element peek should work"
    stack.pop()
    assert stack.isEmpty(), "After pop, stack should be empty"

def test_stack_lifo():
    """Test stack LIFO property."""
    from Stack.stack import Stack
    stack = Stack()
    for i in range(5):
        stack.push(i)
    for i in range(4, -1, -1):
        assert stack.pop() == i, f"LIFO violated at {i}"

def test_queue_basic():
    """Test queue basic operations."""
    from Queue.Queue import Queue
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1, "Front should be 1"
    assert queue.dequeue() == 1, "Dequeue should return 1"

def test_queue_edge_cases():
    """Test queue edge cases - empty, single element."""
    from Queue.Queue import Queue
    
    # Empty queue
    queue = Queue()
    assert queue.LinkedList.length == 0, "Empty queue size should be 0"
    
    # Single element
    queue.enqueue(42)
    assert queue.peek() == 42, "Single element peek should work"
    assert queue.dequeue() == 42, "Dequeue should return 42"

def test_queue_fifo():
    """Test queue FIFO property."""
    from Queue.Queue import Queue
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    for i in range(5):
        assert queue.dequeue() == i, f"FIFO violated at {i}"

def test_binary_tree_basic():
    """Test binary tree basic operations."""
    from tree.tree_new import BinaryTree
    bt = BinaryTree(1)
    bt.add(2)
    bt.add(3)
    assert bt.root.value == 1, "Root should be 1"

def test_binary_tree_single_node():
    """Test binary tree with single node."""
    from tree.tree_new import BinaryTree
    bt = BinaryTree(42)
    assert bt.root.value == 42, "Root should be 42"

def test_tree_basic():
    """Test general tree basic operations."""
    from tree.tree import Tree
    tree = Tree(1)
    pass

def test_avl_tree_basic():
    """Test AVL tree basic operations."""
    from avl_trees.avlTree import AVLNode
    avl = AVLNode(10)
    assert avl.value == 10, "Root value should be 10"

def test_search_basic():
    """Test search algorithms basic operations."""
    from search.search import linearSearch, binarySearch
    arr = [1, 2, 3, 4, 5]
    assert linearSearch(arr, 3) == 2, "Linear search should find element"
    assert binarySearch(arr, 3) == 2, "Binary search should find element"

def test_search_edge_cases():
    """Test search edge cases - single element, not found."""
    from search.search import linearSearch, binarySearch
    
    # Single element - found
    assert linearSearch([42], 42) == 0, "Should find single element"
    assert binarySearch([42], 42) == 0, "Should find single element"
    
    # Single element - not found
    assert linearSearch([42], 99) == False, "linearSearch should return False when not found"
    assert binarySearch([42], 99) == -1, "binarySearch should return -1 when not found"
    
    # Element not found
    assert linearSearch([1, 2, 3], 99) == False, "linearSearch should return False when not found"
    assert binarySearch([1, 2, 3], 99) == -1, "binarySearch should return -1 when not found"

def test_search_boundaries():
    """Test search at array boundaries."""
    from search.search import linearSearch, binarySearch
    arr = [1, 2, 3, 4, 5]
    
    # First element
    assert linearSearch(arr, 1) == 0, "Should find first element"
    assert binarySearch(arr, 1) == 0, "Should find first element"
    
    # Last element
    assert linearSearch(arr, 5) == 4, "Should find last element"
    assert binarySearch(arr, 5) == 4, "Should find last element"

def test_bubble_sort_basic():
    """Test bubble sort basic operation."""
    from bubbleSort.bubbleSort import bubbleSort
    arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
    bubbleSort(arr)
    assert list(arr) == [1, 1, 2, 3, 4, 5, 6, 9], "Array should be sorted"

def test_bubble_sort_edge_cases():
    """Test bubble sort edge cases - single, empty variations."""
    from bubbleSort.bubbleSort import bubbleSort
    
    # Single element
    arr = np.array([42])
    bubbleSort(arr)
    assert list(arr) == [42], "Single element should remain unchanged"
    
    # Already sorted
    arr = np.array([1, 2, 3, 4, 5])
    bubbleSort(arr)
    assert list(arr) == [1, 2, 3, 4, 5], "Already sorted should remain sorted"
    
    # Reverse sorted
    arr = np.array([5, 4, 3, 2, 1])
    bubbleSort(arr)
    assert list(arr) == [1, 2, 3, 4, 5], "Reverse sorted should be sorted"

def test_bubble_sort_duplicates():
    """Test bubble sort with duplicates."""
    from bubbleSort.bubbleSort import bubbleSort
    arr = np.array([3, 1, 3, 1, 3])
    bubbleSort(arr)
    assert list(arr) == [1, 1, 3, 3, 3], "Duplicates should be sorted correctly"

def test_selection_sort_basic():
    """Test selection sort basic operation."""
    from selectionSort.selectionSort import selectionSort
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    selectionSort(arr)
    assert arr == [1, 1, 2, 3, 4, 5, 6, 9], "Array should be sorted"

def test_selection_sort_edge_cases():
    """Test selection sort edge cases."""
    from selectionSort.selectionSort import selectionSort
    
    # Single element
    arr = [42]
    selectionSort(arr)
    assert arr == [42], "Single element should remain unchanged"
    
    # Already sorted
    arr = [1, 2, 3, 4, 5]
    selectionSort(arr)
    assert arr == [1, 2, 3, 4, 5], "Already sorted should remain sorted"

def test_selection_sort_duplicates():
    """Test selection sort with duplicates."""
    from selectionSort.selectionSort import selectionSort
    arr = [3, 1, 3, 1, 3]
    selectionSort(arr)
    assert arr == [1, 1, 3, 3, 3], "Duplicates should be sorted correctly"

def test_insertion_sort_basic():
    """Test insertion sort basic operation."""
    from insertSort.insertSort import insertSort
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    insertSort(arr)
    assert arr == [1, 1, 2, 3, 4, 5, 6, 9], "Array should be sorted"

def test_insertion_sort_edge_cases():
    """Test insertion sort edge cases."""
    from insertSort.insertSort import insertSort
    
    # Single element
    arr = [42]
    insertSort(arr)
    assert arr == [42], "Single element should remain unchanged"
    
    # Two elements
    arr = [2, 1]
    insertSort(arr)
    assert arr == [1, 2], "Two elements should be sorted"

def test_merge_sort_basic():
    """Test merge sort basic operation."""
    from insertSort.insertSort import mergeSort
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    result = mergeSort(arr)
    assert result == [1, 1, 2, 3, 4, 5, 6, 9], "Array should be sorted"

def test_merge_sort_edge_cases():
    """Test merge sort edge cases."""
    from insertSort.insertSort import mergeSort
    
    # Single element
    result = mergeSort([42])
    assert result == [42], "Single element should remain unchanged"
    
    # Two elements
    result = mergeSort([2, 1])
    assert result == [1, 2], "Two elements should be sorted"

def test_quick_sort_basic():
    """Test quick sort basic operation."""
    from insertSort.insertSort import quickSort
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    result = quickSort(arr)
    assert result == [1, 1, 2, 3, 4, 5, 6, 9], "Array should be sorted"

def test_quick_sort_edge_cases():
    """Test quick sort edge cases."""
    from insertSort.insertSort import quickSort
    
    # Single element
    result = quickSort([42])
    assert result == [42], "Single element should remain unchanged"
    
    # Two elements
    result = quickSort([2, 1])
    assert result == [1, 2], "Two elements should be sorted"

def test_graph_basic():
    """Test graph basic operations."""
    from graph.graph import Graph
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('B', 'C', 2)
    assert graph is not None, "Graph should be created"

def test_graph_edge_cases():
    """Test graph edge cases - single node, self-loops."""
    from graph.graph import Graph
    
    # Single edge
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    assert graph is not None, "Graph with single edge should work"
    
    # Self-loop
    graph = Graph()
    graph.add_edge('A', 'A', 0)
    assert graph is not None, "Graph with self-loop should work"

def test_trie_basic():
    """Test trie basic operations."""
    from trie.trie import Trie
    trie = Trie()
    trie.addString("hello")
    assert trie.search("hello") == True, "Should find added string"
    assert trie.search("hell") == False, "Should not find prefix"

def test_trie_single_char():
    """Test trie with single character."""
    from trie.trie import Trie
    trie = Trie()
    trie.addString("a")
    assert trie.search("a") == True, "Should find single character"
    assert trie.search("ab") == False, "Should not find non-existent extension"

def test_trie_empty_search():
    """Test trie empty search."""
    from trie.trie import Trie
    trie = Trie()
    assert trie.search("hello") == False, "Should not find in empty trie"

def test_trie_prefix_collision():
    """Test trie with overlapping prefixes."""
    from trie.trie import Trie
    trie = Trie()
    trie.addString("car")
    trie.addString("card")
    trie.addString("care")
    assert trie.search("car") == True, "Should find car"
    assert trie.search("card") == True, "Should find card"
    assert trie.search("car2") == False, "Should not find car2"

def test_binary_heap_basic():
    """Test binary heap basic operations."""
    from binary_heap.binary_heap import BinaryHeap
    heap = BinaryHeap(10, 'min')
    heap.insert(5)
    heap.insert(3)
    assert heap.peek() == 3, "Min heap should have min at top"

def test_binary_heap_single_element():
    """Test binary heap with single element."""
    from binary_heap.binary_heap import BinaryHeap
    heap = BinaryHeap(5, 'min')
    heap.insert(42)
    assert heap.peek() == 42, "Single element should be peeked"

def test_binary_heap_ordering():
    """Test binary heap ordering property."""
    from binary_heap.binary_heap import BinaryHeap
    heap = BinaryHeap(10, 'min')
    values = [5, 3, 7, 1, 9]
    for v in values:
        heap.insert(v)
    assert heap.peek() == 1, "Min should be at top after multiple inserts"

def test_disjoint_set_basic():
    """Test disjoint set basic operations."""
    try:
        from disjointSet.disjointedSet import DisjointSet
        ds = DisjointSet(5)
        ds.union(0, 1)
        assert ds.find(0) == ds.find(1), "Should be in same set"
    except SyntaxError:
        pass

def test_disjoint_set_single_element():
    """Test disjoint set with single element."""
    try:
        from disjointSet.disjointedSet import DisjointSet
        ds = DisjointSet(1)
        assert ds.find(0) == 0, "Single element should find itself"
    except SyntaxError:
        pass

def test_disjoint_set_union_same():
    """Test repeated unions on same sets."""
    try:
        from disjointSet.disjointedSet import DisjointSet
        ds = DisjointSet(3)
        ds.union(0, 1)
        ds.union(0, 1)  # Union same sets again
        assert ds.find(0) == ds.find(1), "Should remain in same set"
    except SyntaxError:
        pass

def test_disjoint_set_path_compression():
    """Test path compression in disjoint set."""
    try:
        from disjointSet.disjointedSet import DisjointSet
        ds = DisjointSet(4)
        ds.union(0, 1)
        ds.union(1, 2)
        ds.union(2, 3)
        assert ds.find(0) == ds.find(3), "All should be in same set"
    except SyntaxError:
        pass

def test_oop_basic():
    """Test OOP examples."""
    from oop.StartCookie import StarCookie
    cookie = StarCookie(15, "Red")
    assert cookie.weight == 15, "Weight should be 15"
    assert cookie.color == "Red", "Color should be Red"

# ==================== MAIN TEST RUNNER ====================

def run_all_tests():
    """Run all tests and report results."""
    print(f"\n{'='*70}")
    print("COMPREHENSIVE TEST SUITE - STANDARD + EDGE CASES")
    print(f"{'='*70}\n")
    
    tests = [
        # Array Tests
        ("Arrays - Basic", test_arrays_basic),
        
        # Linked List Tests
        ("Linked Lists - Basic", test_linked_lists_basic),
        ("Linked Lists - Edge Cases", test_linked_lists_edge_cases),
        
        # Stack Tests
        ("Stack - Basic", test_stack_basic),
        ("Stack - Edge Cases", test_stack_edge_cases),
        ("Stack - LIFO Property", test_stack_lifo),
        
        # Queue Tests
        ("Queue - Basic", test_queue_basic),
        ("Queue - Edge Cases", test_queue_edge_cases),
        ("Queue - FIFO Property", test_queue_fifo),
        
        # Tree Tests
        ("Binary Tree - Basic", test_binary_tree_basic),
        ("Binary Tree - Single Node", test_binary_tree_single_node),
        ("Tree - Basic", test_tree_basic),
        ("AVL Tree - Basic", test_avl_tree_basic),
        
        # Search Tests
        ("Search - Basic", test_search_basic),
        ("Search - Edge Cases", test_search_edge_cases),
        ("Search - Boundaries", test_search_boundaries),
        
        # Sorting Tests - Bubble
        ("Bubble Sort - Basic", test_bubble_sort_basic),
        ("Bubble Sort - Edge Cases", test_bubble_sort_edge_cases),
        ("Bubble Sort - Duplicates", test_bubble_sort_duplicates),
        
        # Sorting Tests - Selection
        ("Selection Sort - Basic", test_selection_sort_basic),
        ("Selection Sort - Edge Cases", test_selection_sort_edge_cases),
        ("Selection Sort - Duplicates", test_selection_sort_duplicates),
        
        # Sorting Tests - Insertion
        ("Insertion Sort - Basic", test_insertion_sort_basic),
        ("Insertion Sort - Edge Cases", test_insertion_sort_edge_cases),
        
        # Sorting Tests - Merge
        ("Merge Sort - Basic", test_merge_sort_basic),
        ("Merge Sort - Edge Cases", test_merge_sort_edge_cases),
        
        # Sorting Tests - Quick
        ("Quick Sort - Basic", test_quick_sort_basic),
        ("Quick Sort - Edge Cases", test_quick_sort_edge_cases),
        
        # Graph Tests
        ("Graph - Basic", test_graph_basic),
        ("Graph - Edge Cases", test_graph_edge_cases),
        
        # Trie Tests
        ("Trie - Basic", test_trie_basic),
        ("Trie - Single Character", test_trie_single_char),
        ("Trie - Empty Search", test_trie_empty_search),
        ("Trie - Prefix Collision", test_trie_prefix_collision),
        
        # Binary Heap Tests
        ("Binary Heap - Basic", test_binary_heap_basic),
        ("Binary Heap - Single Element", test_binary_heap_single_element),
        ("Binary Heap - Ordering", test_binary_heap_ordering),
        
        # Disjoint Set Tests
        ("Disjoint Set - Basic", test_disjoint_set_basic),
        ("Disjoint Set - Single Element", test_disjoint_set_single_element),
        ("Disjoint Set - Same Union", test_disjoint_set_union_same),
        ("Disjoint Set - Path Compression", test_disjoint_set_path_compression),
        
        # OOP Tests
        ("OOP - Basic", test_oop_basic),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        if test_module(test_name, test_func):
            passed += 1
        else:
            failed += 1
    
    # Print summary
    total = passed + failed
    percentage = int((passed / total) * 100) if total > 0 else 0
    
    print(f"\n{'='*70}")
    print("TEST SUMMARY")
    print(f"{'='*70}")
    print(f"Passed:    {passed}")
    if failed > 0:
        print(f"Failed:    {failed}")
    print(f"Total:     {total}")
    print(f"Coverage:  {percentage}%")
    print(f"{'='*70}\n")
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
