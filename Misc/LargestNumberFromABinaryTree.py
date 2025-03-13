
"""
You have been given a Binary Tree of 'N' nodes where the nodes have integer values.

Your task is to find the largest number that could be formed by concatenating all its nodes values.
"""

from collections import *
from math import *

# Following is the Binary Tree Node class structure:     
class BinaryTreeNode:
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None

def printLargest(root):
    if root is None:
        return ""
    nums = []
    q = deque()
    q.append(root)

    while q:
        s = q.popleft()

        if s.left:
            q.append(s.left)
        if s.right:
            q.append(s.right)
    

        nums.append(str(s.data))
    
    nums.sort(key=lambda x: x*10, reverse=True)
    res = "".join(nums)
    
    return res if res[0] != "0" else "0"