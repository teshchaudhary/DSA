from collections import defaultdict

def func(arr):
    currSum = 0
    prefixSum = defaultdict()
    prefixSum[0] = 1
    res = 0

    for i in arr:
        currSum += i

        if currSum  == 0 or currSum in prefixSum:
            res += prefixSum[currSum]
        
        prefixSum[currSum] += 1