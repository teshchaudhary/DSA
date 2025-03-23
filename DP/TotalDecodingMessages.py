"""
A message containing letters A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

You are given a string digits. You have to determine the total number of ways that message can be decoded.
"""

def countWays(digits):
    if not digits or digits[0] == '0':
        return 0

    n = len(digits)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n + 1):
        one_digit = int(digits[i - 1])
        two_digit = int(digits[i - 2:i])
        
        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    
    return dp[n]
