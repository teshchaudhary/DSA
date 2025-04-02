"""
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
"""

# The idea is to put all the nodes as indexing and for each level get the maximum width by doing right_node_index - left_node_index + 1

# For 0 based indexing do like 
# for left 2*index+1
# for right 2*index+2

# For 1 based indexing do like
# for left 2*index
# for right 2*index+1

# $ are dummy ones to clear the example
# The basic idea is to assume dummy nodes until the last node from right on a level in the case below it is node 7 
# so 7 (13) - 6 (7) + 1 = 7
#                            1 (0)
#                          /       \
#                   3 (1)          2 (2)
#                  /     \        /      \
#             5 (3)    $ (4)   $ (5)   9 (6)
#            /    \           /   \     /    \
#       6 (7)   $ (8)   $ (9)  $ (10) 7 (13)  $ (14)


# $ are dummy ones to clear the example
# The basic idea is to assume dummy nodes until the last node from right on a level in the case below it is node 7 
# so 7 (14) - 6 (7) + 1 = 8
#                            1 (0)
#                          /       \
#                   3 (1)          2 (2)
#                  /     \        /      \
#             5 (3)    $ (4)   $ (5)   9 (6)
#            /    \           /   \     /    \
#       6 (7)   $ (8)   $ (9)  $ (10) $ (13)  7 (14)


from collections import deque

class Solution:
    def widthOfBinaryTree(self, root) -> int:
        max_width = 0
        q = deque()
        q.append((root, 0))

        while q:
            level_length = len(q)
            _, left_node_index = q[0]
            _, right_node_index = q[-1]

            max_width =  max(max_width, right_node_index - left_node_index + 1)

            for _ in range(level_length):
                node, index = q.popleft()

                if node.left:
                    q.append((node.left, 2*index+1))
                
                if node.right:
                    q.append((node.right, 2*index+2))
        
        return max_width