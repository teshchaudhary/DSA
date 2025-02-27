from collections import deque

def printRightView(root):
    if root is None:
        return []
        
    q = deque()
    q.append(root)
    res = []

    while q:
        for i in range(len(q)):
            ele = q.popleft()

            if ele.left:
                q.append(ele.left)
            
            if ele.right:
                q.append(ele.right)
                
        res.append(ele.data)
    
    return res