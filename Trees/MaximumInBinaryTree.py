def func(root):
    if root == None:
        return float[-'inf']
    else:
        return max(root.data, func(root.left), func(root.right))
