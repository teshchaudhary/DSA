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