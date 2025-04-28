from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0
 
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    # If we're at the first row or first column,
                    # the largest square is just the cell itself
                    if i == 0 or j == 0:
                        dp[i][j] =  1
                    
                    # we need to check all three:
                    # dp[i-1][j]
                    # dp[i][j-1]
                    # dp[i-1][j-1]

                    # so that if any 0 comes in between it is not counted in the square formation
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
