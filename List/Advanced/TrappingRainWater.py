# We are given a array of bars and we need to determine maximum amount of water we can hold between the bars

# O(n^2)
# Get minimum of the cornermost bars and then subtract it from the height of current bar
# def func(arr):
#     res = 0
#     l = len(arr)
#     for i in range(1, l-1):
#         leftMax = arr[i]

#         # Getting the height of maximum bar in the left of the current element
#         for j in range(0, i):
#             leftMax = max(leftMax, arr[j])

#         rightMax = arr[j]

#         # Getting the height of maximum bar in the right of the current element
#         for j in range(i+1, l):
#             rightMax = max(rightMax, arr[j])

#         # Getting the minimum of the two bars as the water more than that will spill out
#         # Subtracting the height of current element because bars are not hollow
#         res = res + (min(leftMax, rightMax) - arr[i])

#     return res

# Theta(n)
# Intution is to peprocess the heights of the left most longest bar and the right most longest bar to be compared at a single place so that we don't have to compute them again and again


def func1(arr):
    l = len(arr)
    res = 0
    lMax = [0]*l
    rMax = [0]*l

    # An array to get the left one for an element i in arr[i]
    lMax[0] = arr[0]
    for i in range(1, l):
        lMax[i] = max(arr[i], lMax[i-1])

    # An array to get the left one for an element i in arr[i]
    rMax[l-1] = arr[l-1]
    for i in range(l-2, -1, -1):
        rMax[i] = max(arr[i], rMax[i+1])

    # We start from the second of the start and second last because the water before them or on them will be spilled out

    for i in range(1, l-1):
        res = res + (min(lMax[i], rMax[i]) - arr[i])

    print(lMax)
    print(rMax)
    return res


arr = [5,0,6,2,3]
print(func1(arr))
