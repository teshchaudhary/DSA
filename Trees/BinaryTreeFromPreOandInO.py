class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# O(n^2)
def constructTree(preorder, inorder, in_start, in_end):
    if in_start > in_end:
        return None

    global preorder_index
    root = Node(preorder[preorder_index])
    preorder_index += 1

    if in_start == in_end:
        return root
    
    # Find the index of the root node in inorder traversal
    for idx in range(in_start, in_end + 1):
        if inorder[idx] == root.val:
            break

    root.left = constructTree(preorder, inorder, in_start, idx - 1)
    root.right = constructTree(preorder, inorder, idx + 1, in_end)

    return root

def buildTree(preorder, inorder):
    global preorder_index
    preorder_index = 0

    return constructTree(preorder, inorder, 0, len(inorder) - 1)

# O(n)
def constructTree(preorder, inorder, in_start, in_end):
    if in_start > in_end:
        return None

    global preorder_index
    root = Node(preorder[preorder_index])
    preorder_index += 1

    if in_start == in_end:
        return root
    
    idx = io_map[root.data]

    root.left = constructTree(preorder, inorder, in_start, idx - 1)
    root.right = constructTree(preorder, inorder, idx + 1, in_end)

    return root

def buildTree(preorder, inorder):
    global io_map
    global preorder_index
    preorder_index = 0

    for i in range(len(inorder)):
        io_map[inorder[i]] = i

    return constructTree(preorder, inorder, 0, len(inorder) - 1)