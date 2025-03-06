# O(n^2)
def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))

def diameterOfBinaryTree(root):
    if root is None:
        return 0
    d1 = height(root.left) + height(root.right)
    d2 = diameterOfBinaryTree(root.left)
    d3 = diameterOfBinaryTree(root.right)

    return max(d1, d2, d3)

# O(n)
def diameterOfBinaryTree(root):
    def diameter(node):
        nonlocal res
        if not node:
            return 0
        
        lh = diameter(node.left)
        rh = diameter(node.right)

        res = max(res, lh + rh)

        return 1 + max(lh, rh)
    
    res = 0
    diameter(root)
    return res