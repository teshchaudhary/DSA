def isSubsetSum (arr, sum):
    n = len(arr)
    dp = [[False] * (sum + 1) for _ in range(n + 1)]
    
    # For Sum == 0 each element can make it happen
    for ele in range(n + 1):
        dp[ele][0] = True

    
    for ele_idx in range(1, n + 1):
        for curr_sum in range(1, sum + 1):
            # if current element is greater than the current value of sum then it is not possible with current element, so we are going to skip it and make it value equal to prev element's value
            if arr[ele_idx - 1] > curr_sum:
                dp[ele_idx][curr_sum] = dp[ele_idx - 1][curr_sum]

            # For the subset sum we can either ignore the current element or we can take it a and reduce the curr sum value
            else:
                dp[ele_idx][curr_sum] = dp[ele_idx - 1][curr_sum] or dp[ele_idx - 1][curr_sum - arr[ele_idx - 1]]

    return dp[n][sum]