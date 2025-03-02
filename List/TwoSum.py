# Leetcode
def twoSum(nums, target):
    a = dict()
    for i in range(len(nums)):
        converse = target - nums[i]

        if converse in a:
            return a[converse], i
        
        a[nums[i]] = i

# CodeStudio
def twoSum(arr, target):
    res = []
    freq = {} 
    for num in arr:
        complement = target - num
        if complement in freq and freq[complement] > 0:
            res.append([min(num, complement), max(num, complement)])
            freq[complement] -= 1
        else:
            freq[num] = freq.get(num, 0) + 1 
            
    return res if res else [[-1, -1]]