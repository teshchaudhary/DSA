# Recursion
class Solution:
    def helper(self, egg, floor):
        if floor == 0 or floor == 1:
            return floor

        if egg == 1:
            return floor
        
        min_moves = float('inf')

        for i in range(1, floor+1):
            moves = 1 + max(self.helper(egg-1, i-1), self.helper(egg, floor - i))
            min_moves = min(moves, min_moves)
        
        return min_moves

    def superEggDrop(self, k: int, n: int) -> int:
        return self.helper(k, n)

# Memo
class Solution:
    def helper(self, egg, floor, dp):
        if floor == 0 or floor == 1:
            return floor

        if egg == 1:
            return floor
        
        if dp[egg][floor] != -1:
            return dp[egg][floor]

        min_moves = float('inf')

        for i in range(1, floor+1):
            if dp[egg-1][i-1] != -1:
                broken = dp[egg-1][i-1]
            else:
                broken = self.helper(egg-1, i-1, dp)
                dp[egg-1][i-1] = broken
            
            if dp[egg][floor-i] != -1:
                non_broken = dp[egg][floor-i]
            else:
                non_broken = self.helper(egg, floor - i, dp)
                dp[egg][floor-i] = non_broken

            moves = 1 + max(broken, non_broken)
            min_moves = min(moves, min_moves)
        
        dp[egg][floor] = min_moves
        return dp[egg][floor]

    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[-1 for _ in range(n+1)] for _ in range(k+1)]

        return self.helper(k, n, dp)