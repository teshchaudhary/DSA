# Kadane
# Get sum of all normal contiguous subarray
def MaxSubarraySum(arr):
    res = arr[0]
    maxSum = arr[0]
    
    for i in range(1,len(arr)):
        maxSum = max(maxSum + arr[i], arr[i])
        res = max(res, maxSum)
        
    return res

# The intuition is to find the minmum sum of the subarray
# To get this all we need is to invert all the elements' sign and then get the maximum sum of the subarray
# The maximum circular subarray sum will be the total sum of the array added to the maximum sum of the inverted elements of the array


def circularSubarraySum(arr, n):
    maxSubarraySum = MaxSubarraySum(arr)
    # If each element in the array is negative then the maximum sum will come from this only
    if maxSubarraySum < 0:
        return maxSubarraySum

    arraySum = sum(arr)

    for i in range(len(arr)):
        arr[i] *= -1
    
    maxSubarraySumNegative = MaxSubarraySum(arr)

    # Circular Sum
    maxCircular = arraySum + maxSubarraySumNegative 

    return max(maxSubarraySum, maxCircular)


print(circularSubarraySum([8,-4,3,-5,4], 5))