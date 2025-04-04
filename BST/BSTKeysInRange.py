"""
Given a Binary Search Tree and a range [low, high]. Find all the numbers in the BST that lie in the given range.
Note: Element greater than or equal to root go to the right side.
"""

class Solution:
    def getNumbers(self, root, low, high, l):
        if root is None:
            return
        
        if root.data > low:
            self.getNumbers(root.left, low, high, l)
        
        if low <= root.data <= high:
            l.append(root.data)
            
        if root.data < high:
            self.getNumbers(root.right, low, high, l)
            
            
    def printNearNodes(self, root, low, high):
         l = []
         self.getNumbers(root, low, high, l)
         
         return l