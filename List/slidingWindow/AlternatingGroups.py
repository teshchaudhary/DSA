"""
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
"""

def numberOfAlternatingGroups(colors, k):
    colors = colors + colors[:k-1] # For making circular
    n = len(colors)
    res = 0
    i = 0

    for j in range(1, n):
        if colors[j-1] == colors[j]:
            i = j
        
        if j - i + 1 >= k:
            res += 1

    return res