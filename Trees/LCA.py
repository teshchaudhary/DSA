# Naive Solution
# O(n) + O(n) + O(n) = O(3n) = O(n)

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


def lca(root, n1, n2):
    path1 = []
    path2 = []

    findPath(root, n1, path1)
    findPath(root, n2, path2)

    for i in range(len(path1)):
        if path1[i] != path2[i]:
            break
    
    return path1[i-1]

# Efficient Solution
# O(n)

def find_lca(root, n1, n2):
    # Base Case: If root is None, return None
    if root is None:
        return None

    # Case 1: If the current node is either n1 or n2, return the current node
    if root.value == n1 or root.value == n2:
        return root

    # Recursively search for n1 and n2 in left and right subtrees
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)

    # Case 2: If one subtree contains n1 and the other contains n2, the current node is LCA
    if left_lca and right_lca:
        return root

    # Case 3: If one subtree contains both n1 and n2, continue searching in that subtree
    return left_lca if left_lca is not None else right_lca

    # Case 4: If neither subtree contains n1 or n2, return None (this happens automatically)