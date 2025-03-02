def longest_palindromic_subsequence(string):
    """
    Finds the longest palindromic subsequence (LPS) in a given string.

    The problem is solved using the Longest Common Subsequence (LCS) approach
    by comparing the given string with its reversed version.

    Time Complexity: O(n^2)
    Space Complexity: O(n^2)

    :param string: Input string
    :return: Length of the longest palindromic subsequence
    """
    length = len(string)
    reversed_string = string[::-1]  # Reverse the string
    dp = [[0] * (length + 1) for _ in range(length + 1)]  # DP table

    # Compute LCS between original and reversed string
    for i in range(1, length + 1):
        for j in range(1, length + 1):
            if string[i - 1] == reversed_string[j - 1]:  # Matching characters
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:  # If characters don't match, take max of left or top cell
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[length][length]  # The bottom-right cell contains the LPS length


# Example usage
print(longest_palindromic_subsequence("abb"))  # Output: 2
print(longest_palindromic_subsequence("bbbab"))  # Output: 4
print(longest_palindromic_subsequence("cbbd"))  # Output: 2
