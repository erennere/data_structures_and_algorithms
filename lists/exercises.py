"""
Array manipulation exercises module.

This module contains various practice exercises demonstrating array and list
manipulation techniques including two-sum problems, searching, and permutations.

Exercises Include:
    1. twoSumArray: Find all pairs of indices that sum to each number
    2. secondTwoSum: Find pairs that sum to a target value
    3. findNumber: Find index of a number in an array
    4. permutation: Check if two arrays are permutations of each other

These exercises demonstrate important array processing techniques useful in
algorithmic problem-solving and coding interviews.

Functions:
    twoSumArray(arr): Returns pairs that sum to each element
    secondTwoSum(arr, target): Returns indices of pairs summing to target
    findNumber(arr, target): Finds the index of target value
    permutation(list1, list2): Checks if lists are permutations
"""

####### Exercises
####### Two Sum
import numpy as np

def twoSumArray(arr):
    twoDArray = []
    for i in arr:
        pairs = []
        mid = 0
        if i % 2 == 0:
            mid = int(i / 2)
        else:
            mid = int((i-1) / 2) 

        for j in range(0, mid+1):
            pairs.append((j,i-j))
        twoDArray.append(pairs)
    return twoDArray

arr = [2,5,11,16,91]
twoDArray = twoSumArray(arr)
print(twoDArray)

def secondTwoSum(arr, target):
    result = []
    for i,elm1 in enumerate(arr):
        for j, elm2 in enumerate(arr):
            if elm1 + elm2 == target:
                result.append((i, j))
    return result

arr = [2,5,11,16,91]
twoDArray = secondTwoSum(arr,21)
print(twoDArray)

######## Exercise 2: if array contains:
def findNumber(arr, target):
    for i, elm in enumerate(arr):
        if elm == target:
            print(i)

myArray = [1,4,6,3,64,23,6,3,34,54,765]
print(findNumber(myArray, 23))

######## Exercise: Permutation

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    list1.sort()
    list2.sort()
    
    if list1 == list2:
        return True
    return False

