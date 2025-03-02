def find_ceil_index(subseq, target):
    """
    This function finds the index of the smallest element in `subseq`
    that is greater than or equal to `target`. It uses binary search.
    """
    start = 0
    end = len(subseq) - 1

    while start < end:
        mid = (start + end) // 2

        if subseq[mid] >= target:
            end = mid  # Move left to find the smallest possible valid index
        else:
            start = mid + 1  # Move right

    return end

def longest_increasing_subsequence_length(sequence):
    """
    This function finds the length of the longest increasing subsequence (LIS)
    in the given `sequence` using a dynamic approach with a tail array.

    Time Complexity: O(n log n), where `n` is the length of `sequence`.
    """
    length = len(sequence)
    if length == 0:
        return 0

    # Tail array stores the smallest ending element of increasing subsequences
    tail = [sequence[0]]

    for i in range(1, length):
        if sequence[i] > tail[-1]:
            # If the current element is greater than the last element of `tail`, extend `tail`
            tail.append(sequence[i])
        else:
            # If `sequence[i]` can replace an element in `tail`, find the position and replace it
            tail[find_ceil_index(tail, sequence[i])] = sequence[i]

    # The length of `tail` represents the length of the longest increasing subsequence
    return len(tail)
