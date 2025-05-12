from collections import Counter
class Solution:
    def findEvenNumbers(self, digits):
        d = Counter(digits)
        res = set()

        for i in range(100, 1000, 2):

            nums = [i // 100, (i // 10) % 10, i % 10]
            nd = Counter(nums)

            if d[nums[0]] >= nd[nums[0]] and d[nums[1]] >= nd[nums[1]] and d[nums[2]] >= nd[nums[2]]:
                res.add(i)

        return sorted(res)