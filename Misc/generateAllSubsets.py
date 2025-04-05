# For unique elements
def get_all_subsets(input_list):
    subsets = [[]]
    for element in input_list:
        subsets += [curr + [element] for curr in subsets]
    return subsets

a = [1,2,3,4,5]
print(get_all_subsets(a))

# If elements are repeated
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res