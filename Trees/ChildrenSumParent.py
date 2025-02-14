def isSumProperty(root):
    ld = rd = 0

    if root == None or (root.left == None and root.right == None):
        return 1

    else:
        if root.left != None:
            ld = root.left.data

        if root.right != None:
            rd = root.right.data

    if ((root.data == ld+rd) and (isSumProperty(root.left)) and (isSumProperty(root.right))):
        return 1

    else:
        return 0
