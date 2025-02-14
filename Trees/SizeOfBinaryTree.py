def size(root):
    if root == None:
        return 0

    return size(root.left) + size(root.right) + 1