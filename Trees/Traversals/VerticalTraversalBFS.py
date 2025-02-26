from collections import deque

def vertical_order_traversal(root):
    if root is None:
        return []

    queue = deque()
    vertical_map = {}  # Dictionary to store nodes at each horizontal level
    queue.append((root, 0, 0))  # (node, horizontal_distance, depth)
    min_hd = 0  # Track the minimum horizontal distance

    while queue:
        node, horizontal_distance, depth = queue.popleft()
        min_hd = min(min_hd, horizontal_distance)  # Update minimum horizontal distance
        
        if horizontal_distance not in vertical_map:
            vertical_map[horizontal_distance] = []

        # Store (depth, value) to sort later
        vertical_map[horizontal_distance].append((depth, node.value))

        # Add left and right children to the queue
        if node.left:
            queue.append((node.left, horizontal_distance - 1, depth + 1))
        if node.right:
            queue.append((node.right, horizontal_distance + 1, depth + 1))

    # Extract sorted results in order
    result = []
    while min_hd in vertical_map:
        sorted_values = sorted(vertical_map[min_hd])  # Sort by (depth, then value)
        result.append([value for _, value in sorted_values])  # Extract only values
        min_hd += 1

    return result
