# Given an array arr[] of n integers. Check whether it contains a triplet that sums up to zero. 

# Note: Return 1, if there is at least one triplet following the condition else return 0.


def findTriplets(arr, n):
    # Sorting will segragate the numbers and also in a order of their values
    # We can't use partitioning that will be clear in further explanation
    arr.sort()

    for i in range(n):
        # Points to the negative values if exists
        l = i + 1

        # Point to the posiitve values if exists
        r = n - 1

        # To check every other sum pair
        while l < r:
            add = arr[i] + arr[l] + arr[r]
            if add == 0:
                return True
            
            # It means that negative side is more to increase the l so that a lesser negative number can be checked
            elif add < 0:
                l += 1
            
            # It means that positive side is more to increase the l so that a lesser positive number can be checked
            else:
                r -=1
    
    return False