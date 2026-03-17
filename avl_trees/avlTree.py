"""
AVL Tree implementation module.

This module provides an implementation of an AVL (Adelson-Velsky and Landis) Tree,
a self-balancing binary search tree that maintains logarithmic height through
automatic rebalancing operations.

Key Features:
    - Automatic height balancing
    - Left and right rotations for rebalancing
    - Height update and balance factor calculation
    - Insert, search, and remove operations

Classes:
    AVLNode: Represents a node in the AVL tree with balancing properties

The AVL tree ensures O(log N) time complexity for search, insert, and delete
operations by automatically rebalancing the tree when it becomes unbalanced.
"""

class AVLNode:
    def __init__(self, value):
        """Initialize an AVL tree node.
        
        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.left = None
        self.right = None
        self.height = 0  # leaf node height = 0

    def get_height(self):
        """Get the height of the node.
        
        Returns:
            int: The height of the node, or -1 if None.
        """
        if self is None:
            return -1
        return self.height

    def update_height(self):
        """Update the height of the node based on its children's heights.
        
        The height is set to 1 plus the maximum height of its children.
        """
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = 1 + max(left_height, right_height)

    def rotate_left(self):
        """Perform a left rotation on this node.
        
        Used to rebalance the tree when it becomes right-heavy.
        The right child becomes the parent, and this node becomes the left child.
        
        Returns:
            AVLNode: The new root of the rotated subtree.
        """
        temp = self.right
        self.right = temp.left
        self.update_height()
        temp.left = self
        temp.update_height()
        return temp
        
    def rotate_right(self):
        """Perform a right rotation on this node.
        
        Used to rebalance the tree when it becomes left-heavy.
        The left child becomes the parent, and this node becomes the right child.
        
        Returns:
            AVLNode: The new root of the rotated subtree.
        """
        temp = self.left
        self.left = temp.right
        self.update_height()
        temp.right = self
        temp.update_height()
        return temp

    def add(self, value):
        """Add a value to the AVL tree and rebalance if necessary.
        
        Recursively adds the value while maintaining the binary search tree property,
        then checks the balance factor and performs rotations if needed.
        
        Args:
            value: The value to add to the tree.
        
        Returns:
            AVLNode: The root of the subtree after rebalancing.
        """
        if value < self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = AVLNode(value)
        elif value > self.value:
            if self.right:
                self.right.add(value)
            else:
                self.right = AVLNode(value)
        self.update_height()

        l_height = self.left.height if self.left else -1
        r_height = self.right.height if self.right else -1

        balance = l_height - r_height

        # Left heavy
        if balance > 1:
            # Left Right case
            if value > self.left.value:
                self.left = self.left.rotate_left()
            return self.rotate_right()

        # Right heavy
        if balance < -1:
            # Right Left case
            if value < self.right.value:
                self.right = self.right.rotate_right()
            return self.rotate_left()
        return self
    
    def search(self, value):
        """Search for a value in the AVL tree.
        
        Uses binary search tree property to navigate the tree.
        
        Args:
            value: The value to search for.
        
        Returns:
            AVLNode: The node containing the value, or None if not found.
        """
        if value == self.value:
            return self
        elif value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return None
        elif value > self.value:
            if self.right:
                return self.right.search(value)
            else:
                return None
        else:
            return None
    
    def remove(self, value):
        """Remove a value from the AVL tree (implementation started).
        
        Args:
            value: The value to remove.
        
        Returns:
            int: -1 if node not found, otherwise the operation result.
        """
        result = self.search(value)
        if result is None:
            return -1
        


