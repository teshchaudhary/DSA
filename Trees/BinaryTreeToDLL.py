# Binary Tree Node Class
def BTtoDLL(root):
    # prev, head = None, None  
    prev_or_head = [None, None]
    def inOrder(root):
        # nonlocal prev, head
        if root is None:
            return
        
        inOrder(root.left)

        # if prev is None:
        #     head = root
        if prev_or_head[0] is None:
            prev_or_head[1] = root
        # else:
        #     root.left = prev
        #     prev.right = root
        else:
            root.left = prev_or_head[0]
            prev_or_head[0].right = root

        # prev = root
        prev_or_head[0] = root
        inOrder(root.right)

    inOrder(root)
    # return head
    return prev_or_head[1]