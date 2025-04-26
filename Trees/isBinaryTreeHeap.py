"""
You are given a binary tree, and the task is to determine whether it satisfies the properties of a max-heap.

A binary tree is considered a max-heap if it satisfies the following conditions:

Completeness: Every level of the tree, except possibly the last, is completely filled, and all nodes are as far left as possible.
Max-Heap Property: The value of each node is greater than or equal to the values of its children.
"""

from collections import deque

class Solution:
    def isCompleteTree(self, root):
        q = deque([root])
        seen_null = False
        
        while q:
            node = q.popleft()
            if not node:
                seen_null = True
            else:
                if seen_null:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True

    def isHeapUtil(self, root):
        if root is None:
            return True

        if not root.left and not root.right:
            return True

        if root.left and not root.right:
            return root.data >= root.left.data and self.isHeapUtil(root.left)

        if root.left and root.right:
            return (root.data >= root.left.data and
                    root.data >= root.right.data and
                    self.isHeapUtil(root.left) and
                    self.isHeapUtil(root.right))
       
        return False

    def isHeap(self, root):
        if not root:
            return True
        
        if self.isCompleteTree(root) and self.isHeapUtil(root):
            return True
        return False