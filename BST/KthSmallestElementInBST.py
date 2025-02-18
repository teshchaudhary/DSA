def inOrder(root, l):
    if root is None:
        return None
    
    inOrder(root.left, l)
    l.append(root.val)
    inOrder(root.right, l)

def kthSmallest(root, k):
    a = []
    inOrder(root, a)
    return a[k-1]