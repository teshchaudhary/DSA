# Inversion is if a[i]>a[j], i<j

# Naive Solution

# def cntInvrsns(arr):
#     l = len(arr)
#     count = 0
#     for i in range(l):
#         for j in range(i+1,l):
#             if arr[i]>arr[j]:
#                 count += 1

#     return count

def Countmerge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]

    res = i = j = 0
    k = low

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            a[k] = left[i]

            k += 1
            i += 1

        else:
            # All the elements after will be biggger than second half
            res += (len(left) - i)
            a[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1

    return res


def cntInversions(arr, l, r):
    res = 0
    if r > l:
        mid = (l+r)//2
        res += cntInversions(arr, l, mid)
        res += cntInversions(arr, mid+1, r)
        res += Countmerge(arr, l, mid, r)

    return res


a = [5,4,3,2,1]
print(cntInversions(a, 0, 5))
print(a)