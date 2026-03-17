"""Advanced tree implementations and algorithms module.

This module provides implementations of various tree data structures and related algorithms:
- Queue: Basic queue for tree traversal operations
- Tree: General-purpose tree with arbitrary children
- BinaryNode: Node for binary tree structures
- BinaryTree: Binary search tree with multiple traversal methods
- BinaryTreeFromList: Binary tree representation using array/list

Supported Operations:
    - Multiple tree traversals (preorder, inorder, postorder, breadth-first)
    - Tree manipulation (add, delete, search)
    - Height and depth calculations
    - Permutation generation for string analysis
"""

class Node:
    def __init__(self, data=None):
        """Initialize a queue node.
        
        Args:
            data: The data to store in the node.
        """
        self.data = data
        self.next = None
    
    def __str__(self):
        """Return string representation of the node's data.
        
        Returns:
            str: String representation of the node's data.
        """
        return str(self.data)

class Queue:
    def __init__(self, job=None):
        """Initialize a queue with an optional initial job.
        
        Args:
            job: Initial data to add to the queue (default: None).
        """
        self.size = 0
        self.start = None
        self.end = None
        if job:
            node = Node(job)
            self.start = node
            self.end = node
            self.size += 1

    def enqueue(self, job):
        """Add a job to the end of the queue.
        
        Args:
            job: The data to add to the queue.
        """
        if self.size:
            self.end.next = Node(job)
            self.end = self.end.next
        else:
            self.start = Node(job)
            self.end = self.start
        self.size += 1

    def dequeue(self):
        """Remove and return the first job from the queue.
        
        Returns:
            The data from the front of the queue, or None if empty.
        """
        if not self.size:
            return None
        popped = self.start
        self.start = self.start.next
        popped.next = None
        self.size -= 1
        if self.size == 0:
            self.start = None
            self.end = None
        return popped.data
    
class Tree:
    def __init__(self, data):
        """Initialize a tree node with a root value.
        
        Args:
            data: The root value for this tree node.
        """
        self.root = data
        self.height = 1
        self.degree = 0
        self.children = []
    
    def tree_height(self):
        """Calculate the height of the tree (maximum depth + 1).
        
        Returns:
            int: The height of the tree.
        """
        if self.children == []:
            return 1
        return 1 + max(child.tree_height() for child in self.children)
    
    def tree_degree(self):
        """Get the number of direct children (degree) of this node.
        
        Returns:
            int: The number of direct children.
        """
        return len(self.children)
    
    def addChild(self, Tree):
        """Add a child tree to this tree node.
        
        Updates the degree and height properties after adding the child.
        
        Args:
            Tree: A Tree object to add as a child.
        """
        self.children.append(Tree)
        self.degree = self.tree_degree()
        self.height = self.tree_height()
    
    def __str__(self):
        """Return a formatted string representation of the tree.
        
        Returns:
            str: Indented tree structure representation.
        """
        def printChild(string, tree, level=0):
            for i in range(level):
                string += ' '
            string += str(tree.root) + '\n'
            for child in tree.children:
                string = printChild(string, child, level+1)
            return string    
        return printChild('', self)
    
    def preorder_traverse(self):
        """Perform preorder traversal, printing each node's value.
        
        Visits nodes in preorder: current node, then children.
        """
        print(self.root)
        for child in self.children:
            child.preorder_traverse()

    def postorder_traverse(self):
        """Perform postorder traversal, printing each node's value.
        
        Visits nodes in postorder: children first, then current node.
        """
        for child in self.children:
            child.postorder_traverse()
        print(self.root)

    def breadth_first_traverse(self):
        """Perform breadth-first (level-order) traversal, printing each node's value.
        
        Visits nodes level by level from top to bottom.
        """
        queue = Queue()
        queue.enqueue(self)

        while queue.size > 0:
            node = queue.dequeue()
            if node:
                print(node.root)
                for child in node.children:
                    queue.enqueue(child)
    

food = Tree('food')
meat = Tree('meat burger')
vegan = Tree('vegan burger')
fries = Tree('fries')
soya = Tree('soya burger')
chicken = Tree('chicken burger')
beef = Tree('beef burger')

vegan.addChild(soya)
meat.addChild(chicken)
meat.addChild(beef)
food.addChild(vegan)
food.addChild(meat)
food.addChild(fries)

print(food)
food.breadth_first_traverse()

####################################

class BinaryNode():
    def __init__(self, value):
        """Initialize a binary tree node.
        
        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.left = self.right = None

class BinaryTree():
    def __init__(self, value):
        """Initialize a binary search tree with a root value.
        
        Args:
            value: The root node's value.
        """
        node = BinaryNode(value)
        self.root = node
        self.height = 0

    def add(self, value):
        """Add a value to the binary search tree in its proper position.
        
        Uses binary search tree property: left < parent < right.
        
        Args:
            value: The value to add to the tree.
        """
        def _add(node, value):
            if node.value > value:
                if node.left is not None:
                    _add(node.left, value)
                else:
                    new_node = BinaryNode(value)
                    node.left = new_node
            elif node.value < value:            
                if node.right is not None:
                    _add(node.right, value)
                else:
                    new_node = BinaryNode(value)
                    node.right = new_node
        _add(self.root, value)
    
    def depth(self):
        """Calculate the depth of the tree using breadth-first traversal.
        
        Returns:
            int: The depth (number of levels) of the tree.
        """
        if not self.root:
            return 0

        queue = Queue()
        queue.enqueue(self.root)
        depth = 0

        while queue.size > 0:  # While there are still nodes to process
            level_size = queue.size  # Number of nodes at this level
            for _ in range(level_size):  # Process all nodes at the current level
                node = queue.dequeue()
                if node.left:
                    queue.enqueue(node.left)  # Add left child to queue
                if node.right:
                    queue.enqueue(node.right)  # Add right child to queue
            depth += 1  # Completed processing this level, increment depth

        return depth

    def preorder_traverse(self):
        """Perform preorder traversal, printing each node's value.
        
        Visits nodes in preorder: current node, left subtree, right subtree.
        """
        def _preorder_traverse(node):
            print(node.value)
            if node.left:
                _preorder_traverse(node.left)
            if node.right:
                _preorder_traverse(node.right)
        _preorder_traverse(self.root)

    def postorder_traverse(self):
        """Perform postorder traversal, printing each node's value.
        
        Visits nodes in postorder: left subtree, right subtree, current node.
        """
        def _postorder_traverse(node):
            if node.left:
                _postorder_traverse(node.left)
            if node.right:
                _postorder_traverse(node.right)
            print(node.value)
        _postorder_traverse(self.root)

    def inorder_traverse(self):
        """Perform inorder traversal, printing each node's value.
        
        For binary search trees, produces values in sorted order.
        Visits nodes in inorder: left subtree, current node, right subtree.
        """
        def _inorder_traverse(node):
            if node.left:
                _inorder_traverse(node.left)
            print(node.value)
            if node.right:
                _inorder_traverse(node.right)
        _inorder_traverse(self.root)

    def breadth_first_traverse(self):
        """Perform breadth-first (level-order) traversal, printing each node's value.
        
        Visits nodes level by level from top to bottom, left to right.
        """
        queue = Queue()
        queue.enqueue(self.root)
        while queue.size:
            node = queue.dequeue()
            if node:
                print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    def search(self, value):
        """Search for a value in the binary search tree.
        
        Uses binary search property for efficient searching.
        
        Args:
            value: The value to search for.
        
        Returns:
            bool: True if the value is found, False otherwise.
        """
        def _search(node, value):
            if node is None:
                return False
            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            elif node.value < value:
                return _search(node.right, value)
            return False
        return _search(self.root, value)
    
    
    def __str__(self):
        """Return a formatted string representation of the tree structure.
        
        Returns:
            str: Tree structure with indentation showing parent-child relationships.
        """
        def _str_level(node, level=0, branch=""):
            if node is None:
                return ""

            # Prepare the prefix for the current node
            indent = "    " * level
            result = f"{indent}{branch}{node.value}\n"

            # Recurse for left and right children
            left_str = _str_level(node.left, level + 1, "L-- ")
            right_str = _str_level(node.right, level + 1, "R-- ")

            # Add branches
            if left_str or right_str:
                result += f"{indent}|\n"
                if left_str:
                    result += left_str
                if right_str:
                    result += right_str

            return result

        return _str_level(self.root)

    def delete(self, value):
        """Delete a node with the given value from the binary search tree.
        
        Handles three cases: leaf node, node with one child, node with two children.
        For two children, uses in-order successor for replacement.
        
        Args:
            value: The value of the node to delete.
        """
        def _getMin(node):
            if node is None:
                return None
            if node.left is None:
                return node
            return _getMin(node.left)
        
        def _delete(node, value):
            if node is None:
                return node
            if node.value > value:
                node.left = _delete(node.left, value)  # Search in left subtree
            elif node.value < value:
                node.right = _delete(node.right, value)  # Search in right subtree
            else:
                # Node to be deleted found
                if node.left is None and node.right is None:  # No children
                    return None
                elif node.left is None:  # Only right child
                    return node.right
                elif node.right is None:  # Only left child
                    return node.left
                else:  # Two children
                    min_node = _getMin(node.right)  # Find the in-order successor
                    node.value = min_node.value  # Replace current node value with min_node's value
                    node.right = _delete(node.right, min_node.value)  # Delete the in-order successor
            return node
        
        self.root = _delete(self.root, value)  # Start the delete operation from the root


# Create a binary tree with an initial value
tree = BinaryTree(10)

# Test adding elements
tree.add(5)
tree.add(15)
tree.add(3)
tree.add(7)
tree.add(12)
tree.add(18)

# Test tree structure by printing (str method)
print("Tree structure (str):")
print(tree)

# Test different traversal methods
print("Preorder Traversal:")
tree.preorder_traverse()

print("\nInorder Traversal:")
tree.inorder_traverse()

print("\nPostorder Traversal:")
tree.postorder_traverse()

print("\nBreadth-First Traversal:")
tree.breadth_first_traverse()

# Test the depth of the tree
print("\nDepth of the tree:")
print(tree.depth())

# Test searching for values
print("\nSearching for 7 in the tree:")
print(tree.search(7))  # Should return True

print("\nSearching for 20 in the tree:")
print(tree.search(20))  # Should return False

print(tree)
# Test deleting a node
print("\nDeleting 15 from the tree:")
tree.delete(15)
print(tree)
tree.add(15)

# Test deleting a leaf node
print("\nDeleting leaf node 3 from the tree:")
tree.delete(3)
print(tree)
tree.add(3)

# Test deleting a node with one child
print("\nDeleting node with one child (7):")

tree.delete(7)
print(tree)
tree.add(7)
print(tree)

# Test deleting a node with two children
print("\nDeleting node with two children (5):")
tree.delete(5)
print(tree)


class BinaryTreeFromList:
    def __init__(self, max_size):
        """Initialize a binary tree data structure using a list/array.
        
        Args:
            max_size: The maximum capacity of the tree.
        """
        self.max_size = max_size
        self.list = [None] * max_size

    def add(self, value):
        """Add a value to the tree (implementation placeholder).
        
        Args:
            value: The value to add to the tree.
        """
        if len(self.list) == 0:
            self.list[0] = value
        else:
            pass


def generate_permutations(s, start, length, current, perms):
    """Generate all permutations of a given length from a string.
    
    Uses backtracking to generate all possible permutations by selecting
    characters from the input string recursively.
    
    Args:
        s (str): The input string to generate permutations from.
        start (int): The starting index for selection (used for recursion).
        length (int): The desired length of each permutation.
        current (list): The current permutation being built (accumulator).
        perms (list): The list to store all generated permutations.
    """
    # Base case: if the current permutation reaches the desired length
    if len(current) == length:
        perms.append("".join(current))
        return
    # Generate all permutations by recursively choosing characters
    for i in range(start, len(s)):
        current.append(s[i])
        generate_permutations(s, i + 1, length, current, perms)  # Recur with next character
        current.pop()  # Backtrack

def longest_valid_substring(s):
    """Find the longest substring that does not appear elsewhere in the string.
    
    A valid permutation is one where no character from the permutation
    appears in the remaining portion of the original string.
    
    Args:
        s (str): The input string to analyze.
    
    Returns:
        str: The longest valid substring, or empty string if none exists.
    """
    # Initialize a list to store all valid permutations
    all_permutations = []
    
    # Generate all permutations for lengths from 1 to len(s)-1
    for length in range(1, len(s)):  # Only lengths strictly less than len(s)
        perms = []
        generate_permutations(s, 0, length, [], perms)
        all_permutations.extend(perms)
    
    longest_substring = ""
    
    # Check each permutation to see if it's valid
    for perm_str in all_permutations:
        # Create a set of characters used in the permutation
        used_chars = set(perm_str)
        
        # Create the remaining string by removing used characters from the original string
        remaining_string = s
        for char in perm_str:
            remaining_string = remaining_string.replace(char, '', 1)
        
        # Check that no character from the permutation appears in the remaining string
        valid = True
        for char in perm_str:
            if char in remaining_string:
                valid = False
                break
        
        # If the permutation is valid and its length is greater than the current longest, update it
        if valid and len(perm_str) > len(longest_substring):
            longest_substring = perm_str
    
    return longest_substring

# Example usage
string = "aamanda"
result = longest_valid_substring(string)
print("Longest valid substring:", result)
