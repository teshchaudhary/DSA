class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j = n, m
        scs = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]: 
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  # Move up
                scs.append(str1[i - 1])
                i -= 1
            else:  # Move left
                scs.append(str2[j - 1])
                j -= 1

        # Add remaining characters from both strings
        while i > 0:
            scs.append(str1[i - 1])
            i -= 1
        while j > 0:
            scs.append(str2[j - 1])
            j -= 1

        # Reverse since we constructed the SCS backwards
        return "".join(reversed(scs))