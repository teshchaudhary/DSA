def longest_string_chain(words):
    """
    Finds the length of the longest possible word chain in a given list of words.

    A word chain is a sequence where each word is formed by inserting exactly one character 
    into the previous word while maintaining character order.

    :param words: List of words (strings) consisting of lowercase English letters.
    :return: Length of the longest word chain.
    """

    # Step 1: Sort words based on their length (shorter words first).
    words.sort(key=len)

    # Step 2: Initialize a dictionary to store the longest chain length ending at each word.
    dp = {}
    max_chain_length = 1  # Tracks the longest chain found.

    # Step 3: Process each word and determine the longest chain ending at that word.
    for word in words:
        dp[word] = 1  # each word makes a chain length of 1 (also handles single character strings)

        # Step 4: Generate all possible predecessors by removing one character at a time.
        for i in range(len(word)):
            predecessor = word[:i] + word[i+1:]  # Remove the character at index i.

            # Step 5: If the predecessor exists in our dictionary, update the chain length.
            if predecessor in dp:
                dp[word] = max(dp[word], dp[predecessor] + 1)

        # Step 6: Update the global maximum chain length.
        max_chain_length = max(max_chain_length, dp[word])

    return max_chain_length

words = ["a", "ab", "abc", "abcd", "abcde", "xyz", "xyza", "xyzab"]
print(longest_string_chain(words))  # Output: 5 ["a" → "ab" → "abc" → "abcd" → "abcde"]

words = ["ba", "b", "a", "bca", "bda", "bdca"]
# after sorrting ["a", "b", "ba", "bca", "bda", "bdca"]
print(longest_string_chain(words)) # Output: 4 ["a", "ba", "bda", "bdca"].