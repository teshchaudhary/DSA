from collections import defaultdict

# concept
# if the sum till an index is s and we need to find the subarray sum of K
# we can find the ones between the subarray using s-K

#  so if for s-k a sub existed before it means sum k was made before too

def subarraySum(nums, k):
    pSum_d = defaultdict(int)
    pSum_d[0] = 1 # Needed when first elements itself is making sum
    pSum = 0
    res = 0
    
    for i in nums:
        pSum += i
        back = pSum-k
        res += pSum_d[back]
        pSum_d[pSum] += 1
    
    return res