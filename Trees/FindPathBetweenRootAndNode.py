def findPath(root, x, path):
    if root is None:
        return False
    
    path.append(root.data)

    if root.data == x:
        return True
    
    if (root.left is not None and findPath(root.left, x, path)) or (root.right is not None and findPath(root.right, x, path)):
        return True
    
    path.pop()
    return False
