from collections import deque

# Naive Solution with much extra space
def rightView(self,root):
        res = []
        res_ = []
        if root is None:
            return
        
        q = deque()
     
        q.append(root)
     
        while q:
            
            count = len(q)
    
            while count > 0:
                node = q.popleft()
                
                res_.append(node.data)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    
                    q.append(node.right)
     
                count -= 1
                
            res.append(res_[-1])
            res_.clear()
        
        return res

# Better Solution

def RightView(root):
    if root is None:
        return []
    
    res = []
    q = deque()
    q.append(root)

    while q:
        size = len(q)
        i = 0

        while i < size:
            curr = q.popleft()
            i = i + 1

            if i == size:
                res.append(curr.data)

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)
    return res 