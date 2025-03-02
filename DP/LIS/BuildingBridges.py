def find_ceil_index(seq, target):
    """
    Finds the index of the smallest element in `seq` that is greater than or equal to `target`
    using binary search.

    This function helps maintain an increasing sequence by finding the correct position 
    to replace an element.

    Time Complexity: O(log n)
    """
    start, end = 0, len(seq) - 1

    while start < end:
        mid = (start + end) // 2

        if seq[mid] >= target:
            end = mid  # Move left to find the first occurrence
        else:
            start = mid + 1  # Move right

    return end


def longest_increasing_subsequence(city_pairs):
    """
    Given a list of city pairs (north, south), this function finds the length of the
    Longest Increasing Subsequence (LIS) based on the southern cities.

    This ensures that the maximum number of non-crossing bridges can be built.

    Time Complexity: O(n log n)
    """
    n = len(city_pairs)
    lis_seq = [city_pairs[0][1]]  # Initialize LIS with the first southern city

    for i in range(1, n):
        if city_pairs[i][1] > lis_seq[-1]:
            # Extend the LIS sequence if the new value is larger
            lis_seq.append(city_pairs[i][1])
        else:
            # Find the correct position to replace an element
            lis_seq[find_ceil_index(lis_seq, city_pairs[i][1])] = city_pairs[i][1]

    return len(lis_seq)  # The number of bridges that can be built without crossing


def max_non_crossing_bridges(city_pairs):
    """
    Given a list of city pairs representing bridge connections between 
    north and south banks, this function finds the maximum number of 
    non-crossing bridges that can be built.

    Approach:
    1. Sort the city pairs based on the northern bank positions.
    2. Find the LIS based on the southern bank positions.

    Sorting ensures that bridges do not cross based on northern cities, 
    and LIS ensures the order is maintained for the southern cities.

    Time Complexity: O(n log n)
    """
    city_pairs = sorted(city_pairs, key=lambda x: (x[0], x[1]))  # Sort by northern city

    return longest_increasing_subsequence(city_pairs)


# Example usage
bridges1 = [[6, 2], [4, 3], [2, 6], [1, 5]]
bridges2 = [[8, 1], [1, 2], [4, 5], [3, 4], [2, 6], [6, 7], [7, 8], [5, 5]]

print(max_non_crossing_bridges(bridges1))  # Output: 2
print(max_non_crossing_bridges(bridges2))  # Output: 4
