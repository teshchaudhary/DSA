from collections import deque
def getBottomView(root):
    if not root:
        return []

    q = deque()
    q.append((root, 0))
    vm = {}
    res = []

    while q:
        node, hd = q.popleft()
        
        vm[hd] = node.val
            
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))

    return [vm[hd] for hd in sorted(vm.keys())]