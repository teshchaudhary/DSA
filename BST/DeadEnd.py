def helper(root, low = 1, high = float('inf')):
    if root is None:
        return False
    
    if low == high:
        return True

    return helper(root.left, low, root.data - 1) or helper(root.right, root.data + 1, high)

def isDeadEnd(root):
    return helper(root)