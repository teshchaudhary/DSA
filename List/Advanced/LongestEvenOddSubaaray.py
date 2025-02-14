# Naive Solution
# O(n^2) because we are finding the possibility with each subarray possible

def func0(arr):
    res = 1
    for i in range(len(arr)):
        seq = 1  # Length of sequence being made while condition is True
        for j in range(i+1, len(arr)):
            # Check the proceeding pattern with all possible cases together
            if (arr[j-1] % 2 == 0 and arr[j] % 2 != 0) or \
                    (arr[j-1] % 2 != 0 and arr[j] % 2 == 0):
                seq += 1

            else:
                break  # If pattern is not followed anymore then break and start again with next element

        res = max(res, seq)

    return res


# Efficient Solution
# Kadane's Algorithm

def func1(arr):
    res = 1
    curr = 1

    for i in range(1, len(arr)):
        if (arr[i-1] % 2 == 0 and arr[i] % 2 != 0) or \
                (arr[i-1] % 2 != 0 and arr[i] % 2 == 0):
            curr += 1
            res = max(res, curr)

        else:
            curr = 1

    return res
