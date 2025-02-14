# Naive Partitioning
# O(n) time complexity
# O(n) space complexity
# Stable Partition

# def partitioningArray(arr, idx):
#     l = len(arr)
#     res = []

#     arr[idx], arr[l-1] = arr[l-1], arr[idx]

#     for x in arr:
#         if x <= arr[l-1]:
#             res.append(x)

#     for x in arr:
#         if x > arr[l-1]:
#             res.append(x)

#     for i in range(len(arr)):
#         arr[i] = res[i]


# arr = [1,2,3,8,9,10,7]

# partitioningArray(arr,4)
# print(arr)


# Hoare's Partition
# It moves pivot anywhere but partitions the elements well
# Pivot as first element of array
# Uses first and last element and keep partitioing until both indexes collides
# Fastest partitioning algo
# Unstable Partition

# def HoarePartition(arr, l, h):
#     i = l - 1
#     j = h + 1
#     pivot = arr[l]

#     while True:
#         i += 1
#         while arr[i] < pivot:
#             i += 1

#         j -= 1
#         while arr[j] > pivot:
#             j -= 1

#         if i >= j:
#             return j

#         arr[i], arr[j] = arr[j], arr[i]


# arr = [6, 2, 3, 8, 9, 10]

# HoarePartition(arr, 0, 5)
# print(arr)

# Lomuto's Partition
# It moves pivot to its correct position
# Pivot as last element of array
# paritions as increasing index of smaller and larger indexes
# Unstable Partition

def lomutoPartition(arr,l,h):
    pivot = arr[h]
    i = l - 1

    for j in range(l,h): # We do not consider pivot at first
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1] , arr[h] = arr[h], arr[i+1] # Puts the pivot element in right place

    return i + 1

arr = [6, 2, 3, 8, 9, 10]

lomutoPartition(arr, 0, 5)
print(arr)