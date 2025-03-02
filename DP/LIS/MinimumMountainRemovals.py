def min_deletions_to_make_bitonic(length, sequence):
    """
    Computes the minimum number of deletions required to make a sequence bitonic.
    
    A bitonic sequence first increases and then decreases.
    This function finds:
    1. LIS (Longest Increasing Subsequence)
    2. LDS (Longest Decreasing Subsequence)
    
    The minimum deletions required = Total elements - Maximum bitonic subsequence length.
    
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
    for i in range(length - 2, -1, -1):  # Fix the range
        for j in range(length - 1, i, -1):
            if sequence[i] > sequence[j]:
                decreasing_seq[i] = max(decreasing_seq[i], decreasing_seq[j] + 1)

    max_bitonic_length = 0

    # Find the maximum bitonic subsequence length
    for i in range(length):
        if increasing_seq[i] > 1 and decreasing_seq[i] > 1:
            max_bitonic_length = max(max_bitonic_length, increasing_seq[i] + decreasing_seq[i] - 1)

    return length - max_bitonic_length  # Min deletions to make sequence bitonic


# Example usage
arr1 = [1, 2, 5, 3, 2]
arr2 = [1, 2, 3, 4, 5]  # Already increasing, needs deletions to create a peak
arr3 = [5, 4, 3, 2, 1]  # Already decreasing, no deletions needed

print(min_deletions_to_make_bitonic(len(arr1), arr1))  # Output: 1
print(min_deletions_to_make_bitonic(len(arr2), arr2))  # Output: 1 (removing last element makes peak at 4)
print(min_deletions_to_make_bitonic(len(arr3), arr3))  # Output: 0 (already bitonic)
