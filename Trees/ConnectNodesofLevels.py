
"""
Given a binary tree, connect the nodes that are at the same level. You'll be given an addition nextRight pointer for the same.

Initially, all the next night pointers point to garbage values. Your function should set these pointers to the point next right for each node.
       10                          10 ------> NULL
      / \                       /      \
     3    5       =>          3 ------> 5 --------> NULL
    / \     \               /   \         \
   4   1     2             4 ->  1 ------> 2 -------> NULL
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root):
        if root is None:
            return None

        q = deque()
        q.append(root)
        
        while q:
            prev = None
            
            for _ in range(len(q)):
                s = q.popleft()
                
                if prev:
                    prev.next = s
                
                prev = s
                
                if s.left:
                    q.append(s.left)
                
                if s.right:
                    q.append(s.right)
                
        return root