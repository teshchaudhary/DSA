# Print all the nodes at distance k

def printAtK(root, k):

    if root == None:
        return

    if k == 0:
        print(root.data, end = " ")

    else:
        printAtK(root.left, k-1)
        printAtK(root.right, k-1)
