from collections import deque

def leftView(root):
    q = deque()
    q.append(root)
    res = []

    while q:
        for i in range(len(q)):
            ele = q.popleft()

            if i == 0:
                res.append(ele.data)

            if ele.left:
                q.append(ele.left)
            
            if ele.right:
                q.append(ele.right)

    return res