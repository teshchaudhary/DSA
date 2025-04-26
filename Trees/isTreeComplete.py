
# Intuition:
# if at any level we encounter a null but there are still nodes after it, it means it is not a complete binary tree

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