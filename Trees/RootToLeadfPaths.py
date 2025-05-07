"""
Given a Binary Tree, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

Note: The paths should be returned such that paths from the left subtree of any node are listed first, followed by paths from the right subtree.
"""

# Input: root[] = [1, 2, 3, 4, 5, N, N]
# Output: [[1, 2, 4], [1, 2, 5], [1, 3]]

class Solution:
    
    def dfs(self, root, path, l):
        
        if root is None:
            return
        
        path.append(root.data)
        
        if not root.left and not root.right:
            l.append(list(path))
        
        else:
            self.dfs(root.left, path, l)
            self.dfs(root.right, path, l)
        path.pop()
        
    def Paths(self, root):
        res = []
        self.dfs(root, [], res)
        
        return res