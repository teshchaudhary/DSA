def minimumNumberOfCoins(coins, numberOfCoins, value):
    # Step 1: Initialize the DP array
    # dp[i] represents the minimum number of coins required to form the value 'i'
    dp = [float('inf')] * (value + 1)  # Set all values to "infinity" (unreachable initially)
    dp[0] = 0  # Base case: No coins are needed to make value 0

    # Step 2: Iterate through each value from 1 to 'value'
    for val in range(1, value + 1):
        
        # Step 3: Try using each coin and update dp[val] accordingly
        for coin in coins:  # Directly iterate over available coin denominations
            
            if val >= coin:  # The coin should be usable (cannot exceed the current value)
                
                # Either:
                # 1. We do NOT use this coin → Keep dp[val] as is.
                # 2. We USE this coin → 1 + dp[val - coin] (taking one coin and solving for the remaining amount)
                dp[val] = min(dp[val], 1 + dp[val - coin])

    # Step 4: If dp[value] is still 'inf', it means the value cannot be formed using given coins
    return dp[value] if dp[value] != float('inf') else -1
