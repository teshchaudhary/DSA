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
