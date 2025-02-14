from collections import deque
def LeftView(root):
    res = []
    q = deque()
    q.append(root)

    while q:
        i = len(q)

        while i > 0:
            
            node = q.popleft()
            if i == 1:
                res.append(node.data)
            
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)

            i -= 1
    
    return res