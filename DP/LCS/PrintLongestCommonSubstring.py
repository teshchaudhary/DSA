def longestCommonSubstr(s1, s2):
    n = len(s1)
    m = len(s2)
    
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    max_length = 0  # To store length of the longest common substring
    end_index = 0  # To store the ending index of the longest common substring in s1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                
                # Update max_length and ending index if a longer substring is found
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    # Extract the longest common substring using the ending index and max_length
    longest_common_substr = s1[end_index - max_length:end_index]
    return longest_common_substr

print(longestCommonSubstr("abcdxyz", "xyzabcd"))
