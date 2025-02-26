from collections import deque

def getMaxWidth(root):
    if not root:
        return 0
    
    q = deque()
    q.append(root)
    
    max_width = 0
    
    while q:
        level_width = len(q)
        max_width = max(max_width, level_width)
        
        # Process nodes at the current level
        for i in range(level_width):
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    return max_width
