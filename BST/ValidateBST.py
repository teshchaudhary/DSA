def validateBST(root):
    def isValid(node, min_val, max_val):
        if node is None:
            return True

        if not (min_val < node.data < max_val):
            return False

        return isValid(node.left, min_val, node.data) and isValid(node.right, node.data, max_val)

    return isValid(root, float('-inf'), float('inf'))