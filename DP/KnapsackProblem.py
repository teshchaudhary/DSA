def knapsack(capacity, weights, values):
    n = len(values)

    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    # when we talk about i = 1 an cap(knapsack capcity) = 1
    # it means that we have first object having weight of the first object the capacity is 1
    for i in range(1, n+1):  # Iterate through items
        for cap in range(1, capacity+1):  # Iterate through capacities
            if weights[i-1] > cap:
                dp[i][cap] = dp[i-1][cap]
            else:
                # dp[i-1][cap]: ignore the last item
                # dp[i-1][cap - weights[i-1]]: consider the last item
                # If we are considering the last item it means we need to add its value too
                dp[i][cap] = max(dp[i-1][cap], values[i-1] + dp[i-1][cap - weights[i-1]])

    return dp[n][capacity]

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack(capacity, weights, values))  # Output: 7
