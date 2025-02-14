def maxLevelSum(root):
    l = []
    currentlevel = 0
    queue = []
    queue.append(root)

    while len(queue) > 0:

        current_level_nodes_l = len(queue)
        current_LevelSum = 0

        for _ in range(current_level_nodes_l):
            remove = queue.pop(0)
            current_LevelSum += remove.val

            if remove.left is not None:
                queue.append(remove.left)

            if remove.right is not None:
                queue.append(remove.right)

        l.append(current_LevelSum)

        currentlevel += 1

    return l.index(max(l)) + 1
