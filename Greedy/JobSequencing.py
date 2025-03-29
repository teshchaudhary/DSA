"""
You are given two arrays: deadline[], and profit[], which represent a set of jobs, where each job is associated with a deadline, and a profit. Each job takes 1 unit of time to complete, and only one job can be scheduled at a time. You will earn the profit associated with a job only if it is completed by its deadline.

Your task is to find:

The maximum number of jobs that can be completed within their deadlines.
The total maximum profit earned by completing those jobs.
"""

import heapq

class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        jobs = [(deadline[i], profit[i]) for i in range(n)]
        jobs.sort(key = lambda job: job[0])
        
        min_heap = []
        for deadline, profit in jobs:
            heapq.heappush(min_heap, profit)
            if len(min_heap) > deadline:
                heapq.heappop(min_heap)
        
        max_profit = sum(min_heap)
        max_jobs = len(min_heap)
        
        return [max_jobs, max_profit]