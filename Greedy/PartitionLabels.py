"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
"""


class Solution:
    def partitionLabels(self, s: str):
        # Step 1: Store last occurrences of each character
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i  # Updating the last occurrence of each character
        
        res = []
        start, end = 0, 0
        
        # Step 2: Traverse through the string to determine partitions
        i = 0
        while i < len(s):
            end = max(end, last_index[s[i]])  # Expand partition if needed
            if i == end:  # If reached the end of partition (This will be the partition index)
                res.append(end - start + 1)
                start = i + 1  # Start new partition
            i += 1  # Increment index manually

        return res
