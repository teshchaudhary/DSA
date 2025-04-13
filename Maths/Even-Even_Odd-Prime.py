"""
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
"""

# Even indices (0, 2, 4, ...) must have even digits: {0, 2, 4, 6, 8} → 5 choices
# Odd indices (1, 3, 5, ...) must have prime digits: {2, 3, 5, 7} → 4 choices
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(x, y):
            result = 1
            x = x % MOD
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % MOD
                y = y // 2
                x = (x * x) % MOD
            return result

        even_count = (n + 1) // 2
        odd_count = n // 2
        
        return (power(5, even_count) * power(4, odd_count)) % MOD
