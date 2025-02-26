class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def DFS(node, horizontal_dist, depth, min_hd, vertical_map):
    if node is None:
        return
    
    # Store the current node's value at its corresponding horizontal distance
    if horizontal_dist not in vertical_map:
        vertical_map[horizontal_dist] = []
    vertical_map[horizontal_dist].append(node.data)
    
    # Update the minimum horizontal distance encountered
    min_hd[0] = min(min_hd[0], horizontal_dist)
    
    # Recursively traverse left and right subtrees
    DFS(node.left, horizontal_dist - 1, min_hd, depth+1, vertical_map)  # Move left (decrease HD)
    DFS(node.right, horizontal_dist + 1, min_hd, depth+1, vertical_map) # Move right (increase HD)

def verticalOrder(root):
    # Dictionary to store nodes at each horizontal distance
    vertical_map = {}
    
    # List to track the minimum horizontal distance encountered (as lists are mutable)
    min_hd = [0]

    # Perform DFS traversal to populate the dictionary
    DFS(root, 0, min_hd, vertical_map)
    
    result = []
    current_hd = min_hd[0]

    # Traverse from minimum to maximum horizontal distance and collect results
    while current_hd in vertical_map:
        sorted_values = sorted(vertical_map[current_hd])
        result.append([values for _, values in sorted_values])
        current_hd += 1

    return result


if __name__ == "__main__":
    # Constructing the binary tree:
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    #          \  \
    #           8  9
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    res = verticalOrder(root)
    
    for temp in res:
        print("[", " ".join(map(str, temp)), "]", end=" ")

