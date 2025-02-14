# The array is like there are ranged values in it
# Eg: [[1,4], [3,5]]
# For [1,4]: 1,2,3,4
# For [3,5]: 3,4,5
# So the merged of the overlapped will become [1,5]

# O(nlogn)

def func(arr):
    # Sorting the list with respect to the lower limit of each interval
    arr.sort(key= lambda x: x[0])

    # The index of smallest staring interval
    res = 0

    # i, the index of next coming intervals
    for i in range(1,len(arr)):
        # If the ending of the interval is larger or equal than the starting of the interval of the next range then it means there is a possibility that those can all under a common range

        # Eg: [1,5], [3,7]
        # 5 >= 3 : True
        # We will take the max of 5 or 7 to make it the last limit of the merged interval
        # 7 will be there and the lower limit is going to be the same i.e [1,7]
        if arr[res][1] >= arr[i][0]:
            # Take the upper limit from both of the intervals
            arr[res][1] = max(arr[res][1], arr[i][1])
        
        # If the criteria doesn't fall under the condition, it means that the intervals are disjoint
        # We will just shift the disjoint range towards the last range we encountered
        else:

            # Increase the index of last continuous range so that we can start checking from the new disjoint range
            res += 1

            # Change the value of the nearest interval to last continuous interval
            arr[res] = arr[i]
    
    for i in range(res+1):
        print(arr[i])


arr = [[5,10],[3,15],[18,30],[2,7]]
func(arr)