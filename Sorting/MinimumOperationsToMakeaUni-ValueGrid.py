"""
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
"""

def minOperations(grid):
    arr = []
    rows, columns = len(grid), len(grid[0])

    for row in grid:
        for i in range(columns):
            arr.append(row[i])

    n = rows*columns
    arr.sort()
    median = arr[n//2]
    total_operations = 0

    for ele in arr:
        diff = abs(ele-median)
        if diff % x != 0:
            return -1
        total_operations += diff // x

    return total_operations