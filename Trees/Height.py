# O(h)
def height(root):
    if root == None:
        return 0
    
    return max(height(root.left), root.right) + 1
