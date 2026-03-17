"""
Sum Lists problem implementation module.

This module solves the "Sum Lists" problem where two numbers are represented
as singly linked lists in reverse order, and their sum is calculated.

Problem:
    If two numbers are represented as linked lists in reverse order (e.g.,
    7->1->6 represents 617), add the two numbers and return the sum as a
    linked list in the same reverse order format.

Functions:
    add_two_lists(l1, l2): Adds two numbers represented as linked lists.

Example:
    List1: 9->9->3->4->5->6 = 654399
    List2: 1->2->3->4 = 4321
    Result: 658720 represented as 0->2->7->8->5->6 (in reverse order)

Time Complexity: O(max(len(l1), len(l2)))
Space Complexity: O(max(len(l1), len(l2)))
"""

from LinkedList import LinkedList

def add_two_lists(l1, l2):
    iterator = len(l1)
    l2_length = len(l2)
    current_l1 = l1.head
    current_l2 = l2.head
    
    ll = LinkedList()

    if l2_length > iterator:
        iterator = l2_length

    remain = 0
    for i in range(iterator):
        value = 0
        
        if current_l1:
            value += current_l1.value
            current_l1 = current_l1.next
        if current_l2:
            value += current_l2.value
            current_l2 = current_l2.next
        if remain:
            value += remain
            remain -= 1
        if value >= 10:
            ll.add(int(value % 10))
            remain += 1
        else:
            ll.add(value)
    if remain:
        ll.add(remain)
    return ll

l1 = LinkedList()
l1.add(9)
l1.add(9)
l1.add(3)
l1.add(4)
l1.add(5)
l1.add(6)
print(l1)
l2 = LinkedList()
l2.add(1)
l2.add(2)
l2.add(3)
l2.add(4)
print(l2)
print(add_two_lists(l1, l2))
        
        
        

