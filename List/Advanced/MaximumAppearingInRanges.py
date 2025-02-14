# Given two arrays left and right
# We need to tell the maximum appearing element within the ranges
# ranges will be if first element of left array is 2 and first element of right array is 5 then range will be from 2 to 5 both inclusive

# Naive Solution
# O(N^Max)
# N is the number of ranges
# Max is the last element that can appear (in our case it is 100)

def func1(left, right):
    freq = [0]*100
    for i in range(len(left)):
        for j in range(left[i], right[i]+1):
            freq[j] += 1

    return freq.index(max(freq))

# O(N+Max)
# Making markers


def func2(left, right):
    freq = [0] * 101

    # Put marker 1 for the starting of range
    # Put marker -1 for the ending of range
    for i in range(len(left)):
        freq[left[i]] += 1
        freq[right[i]+1] -= 1

    # Now add up all the marker indexes to get the overlapping elements
    for i in range(1, len(freq)):
        freq[i] = freq[i-1] + freq[i]

    return freq.index(max(freq))

arr1 = [1,2,5,15]
arr2 = [5,8,7,18]
print(func2(arr1,arr2))