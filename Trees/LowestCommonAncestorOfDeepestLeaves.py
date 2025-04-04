"""
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
"""

# This question is same as Smallest Subtree with all the Deepest Nodes

"""
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
"""

from collections import deque

class Solution:
    def find_deepest_leaves(self, root):
        if not root:
            return []

        queue = deque([root])
        first_node, last_node = None, None

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                if i == 0:
                    first_node = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            last_node = node.val

        return first_node, last_node

    def LCA(self, root, n1, n2):
        if root is None or root.val == n1 or root.val == n2:
            return root
        
        left_lca = self.LCA(root.left,n1, n2)
        right_lca = self.LCA(root.right,n1, n2)

        if left_lca and right_lca:
            return root
        
        return left_lca if left_lca is not None else right_lca

    def lcaDeepestLeaves(self, root):
        first_node, last_node = self.find_deepest_leaves(root)

        return self.LCA(root,first_node, last_node)