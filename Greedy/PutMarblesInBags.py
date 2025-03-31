"""
You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.

Divide the marbles into the k bags according to the following rules:

No bag is empty.
If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
The score after distributing the marbles is the sum of the costs of all the k bags.

Return the difference between the maximum and minimum scores among marble distributions.
"""


# Observation:
# We need the sum of adjacent elements only. (Why?)
# Lets take an example [1,2,3,4,5,6,7]

# for each possible partition and suppose currently for k = 2
# suppose partitioned subarrays are

# Partitions      : Scores     Common    Adjacents
# [1][2,3,4,5,6,7]: (1+2+7)  : (1+7)   + (2)
# [1,2][3,4,5,6,7]: (1+2+3+7): (1+7)   + (2+3)
# [1,2,3][4,5,6,7]: (1+3+4+7): (1+7)   + (3+4)
# [1,2,3,4][5,6,7]: (1+4+5+7): (1+7)   + (4+5)
# [1,2,3,4,5][6,7]: (1+5+6+7): (1+7)   + (5+6)
# [1,2,3,4,5,6][7]: (1+6+7)  : (1+7)   + (6)

# so if we find the pair sum for each of the partition and sort them, we can get:
# The maximum scores and minimum scores
# Now just filter out the sum of k maximum and k minimum and their difference is the answer

class Solution:
    def putMarbles(self, weights, k) -> int:
        if k == 1:
            return 0
        
        n = len(weights)

        pair_sums = [weights[i-1] + weights[i] for i in range(1, n)]
        pair_sums.sort()

        mn = sum(pair_sums[:k - 1])
        mx = sum(pair_sums[-(k - 1):])

        return mx - mn