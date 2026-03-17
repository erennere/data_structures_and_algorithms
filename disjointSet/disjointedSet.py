"""
Disjoint Set (Union-Find) data structure implementation.

This module provides an efficient implementation of a Disjoint Set (also known as
Union-Find) data structure with path compression and union by rank optimizations.

A Disjoint Set efficiently maintains a partition of a set of elements, supporting
two main operations:
    - find(x): Determines which set contains an element
    - union(a, b): Merges the sets containing two elements

Optimizations:
    - Path compression: Flattens tree structure during find operations
    - Union by rank: Always attaches smaller trees under larger trees

Classes:
    DisjointSet: Implementation with parent pointers and rank array

Time Complexity: Nearly O(1) amortized time for both operations
"""

class DisjointSet:
    def __init__(self, n):
        # parent[i] = parent of i
        # initially each element is its own parent (root)
        self.parent = list(range(n))
        # rank[i] = approximate tree height
        self.rank = [0] * n

    def find(self, x):
        # find the root with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False  # already in same set

        # union by rank
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True

