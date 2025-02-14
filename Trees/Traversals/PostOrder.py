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
