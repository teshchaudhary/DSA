# Recursion
def postOrder(root, l):
    if root == None:
        return

    postOrder(root.left, l)
    postOrder(root.right, l)
    l.append(root.data)


def listMaker(root):
    l = []
    postOrder(root)

    return l

# Iteration
def postOrder(root):
    stack = [root]
    res = []

    while stack:
        s = stack.pop()
        
        if s.left:
            stack.append(s.left)
        
        if s.right:
            stack.append(s.right)
            
        res.append(s.data)
            
    
    return res[::-1]