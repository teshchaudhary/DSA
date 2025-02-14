# A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree.

def check(root):
    if root is None:
        return 0

    lh = check(root.left)
    if lh == -1:
        return -1

    rh = check(root.right)
    if rh == -1:
        return -1

    if abs(lh-rh) > 1:
        return -1

    else:
        return max(lh, rh) + 1


class Solution:
    def isBalanced(self, root):
        if root is None:
            return True

        c = check(root)

        if c == -1:
            return False

        return True
