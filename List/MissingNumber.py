# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

def MissingNumber(array, n):
    s = (n)*(n+1)//2

    for i in array:
        s -= i

    return s
