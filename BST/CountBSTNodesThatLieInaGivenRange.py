"""
Given a Binary Search Tree (BST) and a range l-h (inclusive), your task is to return the number of nodes in the BST whose value lie in the given range.
"""

class Solution:
    def getCount(self, root, l, h):
        
        if root is None:
            return 0
        
        lc = self.getCount(root.left, l, h)
        rc = self.getCount(root.right, l, h)
        
        # if the node's data is within range we can find more nodes in both left and right
        if l <= root.data <= h:
            return 1 + lc + rc
        
        # if node's data is greater than h then there is no need to look rightwards
        elif root.data > h:
            return lc
        
        # if node's data is smaller than l then there is no need to look leftwards
        else:
            return rc