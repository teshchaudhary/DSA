"""
You are given an array 'ARR' consisting of 'N' positive numbers and sorted in non-decreasing order, and your task is to find the smallest positive integer value that cannot be represented as a sum of elements of any proper subset of the given array.

An array 'B' is a subset of another array 'A' if each element of 'B' is present in 'A'.

For example:
For the given input array [1, 1, 3],
1 can be represented as the sum of elements of the subset [1],
2 can be represented as the sum of elements of a subset [1, 1],
3 can be represented as the sum of elements of a subset [3],
4 can be represented as the sum of elements of a subset [1, 3],
5 can be represented as the sum of elements of a subset [1, 1, 3]
So, the smallest positive integer value that cannot be represented as a sum of elements of any subset of a given array is 6.
"""

def findSmallestInteger(arr):
    smallest_unreachable = 1

    for num in arr:
        if num > smallest_unreachable:
            break
        
        smallest_unreachable +=  num
    
    return smallest_unreachable