# O(h)
def height(root):
    if root == None:
        return 0
    
    return max(height(root.left), root.right) + 1

# O(logn*logn)

def countNodes(root):
    if root is None:
        return 0

    lh, rh = 0, 0
    curr = root
    while curr:
        lh += 1
        curr = curr.left

    curr = root
    while curr:
        rh += 1
        curr = curr.right
    
    if lh == rh:
        return (1<<lh)-1
    
    return 1 + countNodes(root.left) + countNodes(root.right)