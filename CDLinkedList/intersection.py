"""
Linked List Intersection problem implementation module.

This module solves the problem of finding the intersection node of two
singly linked lists that may converge at some point.

Problem:
    Given two singly linked lists that may intersect (share nodes),
    return the node where they intersect. If they don't intersect, return None.

Key Insight:
    If two lists intersect, their tail nodes must be identical. The algorithm
    uses this property to find the intersection point.

Functions:
    intersection(l1, l2): Returns the node where two lists intersect, or None.
    loop(l1_current, l2_current, len1, len2): Helper to find intersection node.

Approach:
    1. Check if both lists share the same tail node
    2. Align pointers by skipping excess nodes in the longer list
    3. Move both pointers until they meet at the intersection

Time Complexity: O(N + M) where N and M are the lengths of the two lists
Space Complexity: O(1) - only uses pointer variables
"""

from LinkedList import LinkedList

def intersection(l1, l2):
    if not isinstance(l1, LinkedList) or not isinstance(l2, LinkedList):
        raise TypeError('not LinkedLists')
    
    def loop(l1_current, l2_current, len1, len2): 
        while l1_current or l2_current:
            for i in range(len1-len2):
                l1_current = l1_current.next
            if l1_current.value == l2_current.value:
                return l1_current
            l1_current = l1_current.next
            l2_current = l2_current.next
        return None

    l1_length = len(l1)
    l2_length = len(l2)
    
    if l1.tail != l2.tail:
        return False
    else:
        l1_current = l1.head
        l2_current = l2.head

        if l1_length >= l2_length:
            node = loop(l1_current, l2_current, l1_length, l2_length)
        else:
            node = loop(l2_current, l1_current, l2_length, l1_length)
    return node


l1 = LinkedList()
l1.add(4)
l1.add(4)
l1.add(4)
l1.add(4)
l1.add(9)
l1.add(5)
l1.add(6)
l1.add(7)
l1.add(3)

current_node = l1.head
l2 = LinkedList()
for i in range(len(l1)):
    current_node = current_node.next
    if i == 3:
        break

l2.head = current_node
l2.tail = l1.tail
l2.length = len(l1) - 3
print(l2)
print(len(l2))
print(intersection(l1, l2))
        


