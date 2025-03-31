# Recursion
def preOrder(root, l):
    if root == None:
        return

    l.append(root.data)
    preOrder(root.left, l)
    preOrder(root.right, l)


def listMaker(root):
    l = []
    preOrder(root)

    return l

# Iteration
def preorder(root):
    stack = [root]
    res = []
    
    while stack:
        s = stack.pop()
        
        res.append(s.data)
        
        if s.right:
            stack.append(s.right)
            
        if s.left:
            stack.append(s.left)
    
    return res