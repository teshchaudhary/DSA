# Function to check if there is a dead-end in a Binary Search Tree (BST)
# A dead-end in a BST means a node exists where no more nodes can be added 
# because both `low` and `high` boundaries are the same.

def helper(root, low=1, high=float('inf')): 
    """
    Recursively checks for a dead-end in a Binary Search Tree (BST).

    Parameters:
    - root: The current node being processed.
    - low: The lower bound for the current subtree (defaults to 1).
    - high: The upper bound for the current subtree (defaults to infinity).

    Returns:
    - True if a dead-end is found, otherwise False.
    """
    
    # Base case: If the node is None, return False (no dead-end found)
    if root is None:
        return False

    # If the current node's range is reduced to a single number, it's a dead-end
    if low == high:
        return True  # Dead-end found
    
    # Recursively check the left and right subtrees
    # - Left child: Allowed values are in the range [low, root.data - 1]
    # - Right child: Allowed values are in the range [root.data + 1, high]
    return helper(root.left, low, root.data - 1) or helper(root.right, root.data + 1, high)


def isDeadEnd(root):
    """
    Wrapper function to check if a BST contains a dead-end.

    Parameters:
    - root: The root of the BST.

    Returns:
    - True if a dead-end is found, otherwise False.
    """
    return helper(root)
