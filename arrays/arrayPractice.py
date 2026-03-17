"""
Array operations and manipulation examples.

This module demonstrates various operations on Python arrays and 2D arrays using
the built-in array module and NumPy. It includes examples of:
- Array creation and basic operations (append, insert, extend)
- Array traversal and indexing
- Array modifications (remove, pop, reverse)
- 2D array operations with NumPy (insert, append, delete)
- Array query operations (index, count, buffer_info)

Usage:
    Run this module to see step-by-step demonstrations of array operations.
    Output shows results after each operation.
"""

from array import *

print('Step 1')
my_array = array('i',[1,2,3,4,5])

print('Step 2')
for i in my_array:
    print(i)

print('Step 3')
for i in range(len(my_array)):
    print(my_array[i])

print('Step 4')
my_array.append(6)
print(my_array)

print('Step 5')
my_array.insert(2,10)
print( my_array)

print('Step 6')
second_array = array('i', [2,6,7,4,6,10])
my_array.extend(second_array)
print(my_array)

print('Step 7')
tempList = [45,565,454,3]
my_array.fromlist(tempList)
print(my_array)

print('Step 8')
my_array.remove(5)
print(my_array)

print('Step 9')
my_array.pop()
print(my_array)

print('Step 10')
print(my_array.index(4))

print('Step 11')
my_array.reverse()
print(my_array)

print('Step 12')
print(my_array.buffer_info())

print('Step 13')
print(my_array.count(4))

print('Step 14')
strTemp = my_array.tobytes()
print(strTemp)

listTemp = my_array.tolist()
print(listTemp)

########################################
########################################
########################################
################2D ARRAYS###############
import numpy as np

twoDArray = np.array([[12,14,24],[26,27,16],[30,23,23]])
print(twoDArray)
newTwoDArray = np.insert(twoDArray,1,[[4,6,10]],axis=0)
print(newTwoDArray)

secondNewTwoDArray = np.append(twoDArray,[[4,6,7]], axis=0)
print(secondNewTwoDArray)

print(secondNewTwoDArray[0,1])

secondNewTwoDArrayDeleted = np.delete(secondNewTwoDArray, 1, axis=0)
print(secondNewTwoDArrayDeleted)


