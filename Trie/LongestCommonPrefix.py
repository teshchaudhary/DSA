class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = strs[0]

        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""
        
        return prefix