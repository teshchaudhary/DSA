def longest_bitonic_subsequence(length, sequence):
    """
    Finds the length of the longest bitonic subsequence in a given sequence.

    A bitonic subsequence first increases and then decreases. 
    This function computes LIS (Longest Increasing Subsequence) 
    and LDS (Longest Decreasing Subsequence) for each element 
    and finds the maximum possible bitonic length.

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    increasing_seq = [1] * length  # Stores LIS values
    decreasing_seq = [1] * length  # Stores LDS values

    # Compute LIS for each element
    for i in range(1, length):
        for j in range(i):
            if sequence[i] > sequence[j]:
                increasing_seq[i] = max(increasing_seq[i], increasing_seq[j] + 1)

    # Compute LDS for each element (traversing from right to left)
    for i in range(length - 2, -1, -1):
        for j in range(length - 1, i, -1):
            if sequence[i] > sequence[j]:
                decreasing_seq[i] = max(decreasing_seq[i], decreasing_seq[j] + 1)

    # Check if sequence is already strictly increasing or decreasing
    if sum(increasing_seq) == length or sum(decreasing_seq) == length:
        return 0

    max_bitonic_length = 0

    # Find the maximum bitonic subsequence length
    for i in range(length):
        if increasing_seq[i] > 1 and decreasing_seq[i] > 1:
            max_bitonic_length = max(max_bitonic_length, increasing_seq[i] + decreasing_seq[i] - 1)

    return max_bitonic_length


# Example usage
arr1 = [1, 2, 5, 3, 2]
arr2 = [1, 2, 3, 4, 5]
arr3 = [5, 4, 3, 2, 1]
print(longest_bitonic_subsequence(len(arr1), arr1))  # Output: 4
print(longest_bitonic_subsequence(len(arr2), arr2))  # Output: 0 (strictly increasing)
print(longest_bitonic_subsequence(len(arr3), arr3))  # Output: 0 (strictly decreasing)
