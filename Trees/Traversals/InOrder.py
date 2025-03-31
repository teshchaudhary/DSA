# Recursion
def inOrder(root, l):
    if root == None:
        return

    inOrder(root.left, l)
    l.append(root.data)
    inOrder(root.right, l)


def listMaker(root):
    l = []
    inOrder(root,l)
    
    return l

# Traversal
def inOrder(root):
    stack = []
    curr = root
    res = []
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        res.append(curr.data)
        curr = curr.right
    
    return res