def lengthOfLongestSubstring(s):
    n = len(s)
    if n == 0:
        return 0
    
    d = {}  # Dictionary to store last seen index of characters
    si = 0  # Left pointer of the sliding window
    res = 0
    
    for ei in range(n):
        # d[s[ei]] >= si is maintaining that we don't go backwards in the string when a repeatig charcter is found
        #example: "cadbzabcd" when we encounter c again (ei = 7) we should not go to the first c again as we have encountered more repeating characters (like a) already so we need to keep it to latest si
        if s[ei] in d and d[s[ei]] >= si:
            si = d[s[ei]] + 1  # Move left pointer `si` to avoid repeating character

        d[s[ei]] = ei  # Update last seen index
        res = max(res, ei - si + 1)  # Update max length

    return res
