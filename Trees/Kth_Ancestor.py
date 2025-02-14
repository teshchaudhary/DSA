from collections import deque

def getParent(root, node):
    q = deque()
    q.append(root)
    p_node = {root.data:None}
    
    while q:
        root = q.popleft()
        
        if root.right:
            p_node[root.right.data] = root.data
            q.append(root.right)
            
            if root.right.data == node:
                break
        
        if root.left:
            p_node[root.left.data] = root.data
            q.append(root.left)
            
            if root.left.data == node:
                break
    
    return p_node
    
def kthAncestor(root,k, node):
    p_dic = getParent(root, node)
    
    for _ in range(k):
        new_p = p_dic.get(node)
        
        if new_p:
            node = new_p
        
        else:
            return -1
    
    return node