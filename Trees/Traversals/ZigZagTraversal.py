from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q = deque()
        q.append(root)
        reverse = False
        res = []
        while q:
            lvl = []
            for _ in range(len(q)):
                s = q.popleft()
                lvl.append(s.val)
                
                if s.left:
                    q.append(s.left)
                
                if s.right:
                    q.append(s.right)
            
            if reverse:
                lvl = lvl[::-1]
                
            res.append(lvl)
            reverse = not reverse
        
        return res