def longest_common_substring(str1, str2):
    """
    Finds the length of the longest common substring (LCS) between two strings.
    
    This function uses dynamic programming to compute the LCS table.

    Time Complexity: O(n^2)
    Space Complexity: O(n^2)

    :param str1: First string
    :param str2: Second string (typically the reversed version of str1 for LPS)
    :return: Length of the longest common substring
    """
    len1, len2 = len(str1), len(str2)
    
    # Initialize DP table
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    longest_length = 0  # Stores the maximum length of common substring

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:  # Matching characters
                dp[i][j] = 1 + dp[i - 1][j - 1]
                longest_length = max(longest_length, dp[i][j])
            else:
                dp[i][j] = 0  # Reset if characters don't match

    return longest_length


# Example usage
input_string = "aacabdkacaa"
reversed_string = input_string[::-1]

print("Reversed String:", reversed_string)
print("Longest Common Substring Length:", longest_common_substring(input_string, reversed_string))
