"""
Tree implementations module.

This module provides implementations of various tree data structures including:
- Tree: General-purpose tree with arbitrary children
- Node: Basic node with value and parent reference
- BinaryNode: Node for binary trees with left and right children
- BinaryTreeFromLL: Binary tree implementation with depth tracking

Classes:
    Node: Represents a tree node with parent reference
    Tree: General tree with multiple children support
    BinaryNode: Node for binary tree structures
    BinaryTreeFromLL: Binary tree with depth tracking

Key Operations:
    - addChild: Add children to tree nodes
    - traverse: Perform tree traversal and return string representation
    - __str__: Display tree structure with formatting
"""

class Node:
    def __init__(self, value, prev):
        """Initialize a tree node.
        
        Args:
            value: The value to store in the node.
            prev: Reference to the parent node.
        """
        self.value = value
        self.prev = prev

    def __str__(self):
        """Return string representation of the node's value.
        
        Returns:
            str: String representation of the node's value.
        """
        return str(self.value)
    
class BinaryNode():
    def  __init__(self, value, left=None, right=None):
        """Initialize a binary tree node.
        
        Args:
            value: The value to store in the node.
            left: Reference to the left child node (default: None).
            right: Reference to the right child node (default: None).
        """
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, node):
        """Initialize a tree with a root node.
        
        Args:
            node: The root Node object for this tree.
        """
        self.node = node
        self.degree = 0
        self.breadth = 0
        self.children = []

    def addChild(self, tree):
        """Add a child tree to this tree.
        
        Links the child tree to this tree by setting its parent reference and
        updating breadth (number of direct children) and degree (maximum depth).
        
        Args:
            tree: A Tree object to add as a child.
        """
        self.children.append(tree)
        tree.node.prev = self.node  # Link parent to child
        self.breadth += 1  # Increment the breadth (direct children)
        # Update the degree (maximum depth) as needed
        self.degree = max(self.degree, tree.degree + 1)

    def traverse(self, level=0):
        """Traverse the tree and return string representation.
        
        Performs a depth-first traversal of the tree, returning a formatted
        string representation with indentation based on tree depth.
        
        Args:
            level (int): Current depth level in the tree (used for indentation).
        
        Returns:
            str: Formatted string representation of the tree structure.
        """
        result = "  " * level + f"Node(value={self.node.value}, degree={self.degree}, breadth={self.breadth}, parent={self.node.prev})\n"
        for child in self.children:
            result += child.traverse(level + 1)
        return result

    def __str__(self):
        """Return string representation of the entire tree.
        
        Returns:
            str: Formatted string representation of the tree structure.
        """
        return self.traverse()

    
# Create nodes
root_node = Node(1, None)
child1_node = Node(2, None)
child11_node = Node(3, None)
child2_node = Node(4, None)
child22_node = Node(5, None)
child222_node = Node(6, None)
# Create trees
root = Tree(root_node)
child1 = Tree(child1_node)
child2 = Tree(child2_node)
child11 = Tree(child11_node)
child22 = Tree(child22_node)
child222 = Tree(child222_node)

# Build tree structure
child1.addChild(child11)
child2.addChild(child22)
child2.addChild(child222)

root.addChild(child1)
root.addChild(child2)

print(root)

class BinaryTreeFromLL:
    def __init__(self, value):
        """Initialize a binary tree node with depth tracking.
        
        Args:
            value: The value to store in the node.
        """
        self.node = BinaryNode(value)
        self.depth = 0

    def addChild(self, tree):
        """Add a child binary tree node.
        
        Adds a child to either the left or right position, raising an exception
        if both positions are already occupied.
        
        Args:
            tree: A BinaryTreeFromLL object to add as a child.
        
        Raises:
            ValueError: If tree is not an instance of BinaryTreeFromLL.
            Exception: If both left and right children are already occupied.
        """
        if not isinstance(tree, BinaryTreeFromLL):
            raise ValueError("addChild expects an instance of BinaryTreeFromLL")

        if self.node.left is None:
            self.node.left = tree.node
            self.depth = max(self.depth, tree.depth + 1)
        elif self.node.right is None:
            self.node.right = tree.node
            self.depth = max(self.depth, tree.depth + 1)
        else:
            raise Exception("Both left and right children are already occupied")

    def __str__(self, level=0):
        """Return formatted string representation of the binary tree.
        
        Performs an in-order traversal with indentation to show tree structure.
        
        Args:
            level (int): Current depth level in the tree (used for indentation).
        
        Returns:
            str: Formatted string representation of the tree.
        """
        result = "  " * level + f"Node(value={self.node.value}, depth={self.depth})\n"
        if self.node.left:
            result += BinaryTreeFromLL(self.node.left.value).__str__(level + 1)
        if self.node.right:
            result += BinaryTreeFromLL(self.node.right.value).__str__(level + 1)
        return result
    
# Create great-grandchildren
great_grandchild1 = BinaryTreeFromLL(8)
great_grandchild2 = BinaryTreeFromLL(9)
great_grandchild3 = BinaryTreeFromLL(10)
great_grandchild4 = BinaryTreeFromLL(11)

# Create grandchildren and add great-grandchildren to them
grandchild1 = BinaryTreeFromLL(4)
grandchild1.addChild(great_grandchild1)
grandchild1.addChild(great_grandchild2)

grandchild2 = BinaryTreeFromLL(5)

grandchild3 = BinaryTreeFromLL(6)

grandchild4 = BinaryTreeFromLL(7)
grandchild4.addChild(great_grandchild3)
grandchild4.addChild(great_grandchild4)

# Create children and add grandchildren to them
child1 = BinaryTreeFromLL(2)
child1.addChild(grandchild1)
child1.addChild(grandchild2)

child2 = BinaryTreeFromLL(3)
child2.addChild(grandchild3)
child2.addChild(grandchild4)

# Create the root and add children to it
root = BinaryTreeFromLL(1)
root.addChild(child1)
root.addChild(child2)

# Print the entire tree
print(root)