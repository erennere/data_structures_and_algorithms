"""Trie (Prefix Tree) data structure implementation.

This module provides a Trie implementation, a tree-like data structure that
stores strings in a way that enables efficient searching, especially for
auto-complete and spell-checking applications.

Key Features:
    - Efficient prefix-based searching
    - O(M) search time where M is the length of the string
    - Support for adding, searching, and deleting strings
    - Memory-efficient for storing many strings with common prefixes

Classes:
    TrieNode: Represents a node in the trie
    Trie: The trie container with string operations
"""

class TrieNode:
    def __init__(self):
        """Initialize a trie node with an empty children dictionary.
        
        Each node can have multiple children, one for each possible character.
        """
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        """Initialize a trie with an empty root node."""
        self.root = TrieNode()

    def addString(self, string):
        """Add a string to the trie.
        
        Traverses or creates nodes for each character in the string,
        marking the final node as the end of a valid word.
        
        Args:
            string (str): The string to add to the trie.
        """
        current_node = self.root
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.end = True

    def search(self, string):
        """Search for a string in the trie.
        
        Returns True only if the exact string exists in the trie.
        
        Args:
            string (str): The string to search for.
        
        Returns:
            bool: True if the string exists, False otherwise.
        """
        current_node = self.root
        for char in string:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.end
        
    def delete(self, string, index=0):
        """Delete a string from the trie.
        
        Recursively removes nodes that are no longer needed after deletion.
        A node is deletable if it has no children and is not the end of another word.
        
        Args:
            string (str): The string to delete.
            index (int): Current index in the string (used for recursion).
        
        Returns:
            bool: True if the node can be deleted, False otherwise.
        """
        if index == len(string):
            if not self.end:
                return False
            self.end = False
            return len(self.children) == 0

        char = string[index]
        if char not in self.children:
            return False
        
        child_note = self.children[char]
        deletable = child_note.delete(string, index + 1)

        if deletable:
            del self.children[char]
            return self.children == 0 and not self.end

        return False


        
        



    