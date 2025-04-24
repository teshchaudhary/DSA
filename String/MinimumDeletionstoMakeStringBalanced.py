"""
You are given a string s consisting only of characters 'a' and 'b'

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.
"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        previous_bs = [0 for i in range(n)]
        ahead_as = [0 for i in range(n)]

        b_count = 0

        for i in range(n):
            previous_bs[i] = b_count

            if s[i] == "b":
                b_count += 1
        
        a_count = 0
        for i in range(n-1,-1,-1):
            ahead_as[i] = a_count

            if s[i] == "a":
                a_count += 1
        
        res = n
        for i in range(n):
            res = min(res, ahead_as[i] + previous_bs[i])

        return res