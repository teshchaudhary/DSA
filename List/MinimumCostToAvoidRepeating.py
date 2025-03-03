def min_cost_to_avoid_repeating(s, cost):
    total_cost = 0  # Tracks the total removal cost
    n = len(s)

    i = 0  # Pointer to traverse the string
    while i < n:
        current_char = s[i]
        max_cost = cost[i]  # Track the highest cost in this duplicate group
        sum_cost = cost[i]  # Sum of all duplicate character costs
        
        # Move through consecutive duplicate characters
        while i + 1 < n and s[i + 1] == current_char:
            i += 1
            sum_cost += cost[i]
            max_cost = max(max_cost, cost[i])
        
        # Add (total cost of duplicates - highest cost) to the answer
        total_cost += (sum_cost - max_cost)
        
        i += 1  # Move to the next new character
    
    return total_cost

# Example Usage
s = "abaac"
cost = [1, 2, 3, 4, 5]
print(min_cost_to_avoid_repeating(s, cost))  # Output: 3
