"""
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.
"""

class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        res = 1 
        for char in s:
            if char in seen:
                res += 1 
                seen.clear()
                
            seen.add(char) 

        return res