# Recursion
class Solution:
    def helper(self, arr, i, j, dp):
        if i == j:
            return 0
            
        mini = float('inf')
        if dp[i][j] != -1:
            return dp[i][j]
            
        for k in range(i, j):
            steps = arr[i-1]*arr[k]*arr[j]\
                    + self.helper(arr, i, k, dp)\
                    + self.helper(arr, k+1, j, dp)
            
            mini = min(mini, steps)
        
        return mini
    
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.helper(arr, 1, n-1, dp)


# Memoization
class Solution:
    def helper(self, arr, i, j, dp):
        if i == j:
            return 0
            
        if dp[i][j] != -1:
            return dp[i][j]
            
        mini = float('inf')
        for k in range(i, j):
            steps = arr[i-1]*arr[k]*arr[j]\
                    + self.helper(arr, i, k, dp)\
                    + self.helper(arr, k+1, j, dp)
            
            mini = min(mini, steps)
        
        dp[i][j] = mini
        return dp[i][j]
    
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.helper(arr, 1, n-1, dp)

# Tabulation
class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for i in range(1, n):
            dp[i][i] = 0
        
        for i in range(n-1, 0, -1):
            for j in range(i+1, n):
                mini = float('inf')
                for k in range(i, j):
                    steps = arr[i-1]*arr[k]*arr[j]+ dp[i][k] + dp[k+1][j]
                    
                    mini = min(mini, steps)
        
                dp[i][j] = mini
    
        return dp[1][n-1]